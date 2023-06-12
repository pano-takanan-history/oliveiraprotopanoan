# Digitizing Proto-Pano

## Introduction

Data in historical linguistics is typically presented in non-machine-readable formats, such as text-based supplementary material or even handwritten manuscripts. Many annotations and important facts are even given in prose, or remain within the linguists head. Those problems make it difficult for non-experts in the specific field to understand the data, and to reproduce and replicate the results, and also limits the exposure the hard work of the linguist gets. Similar to previous blogposts on retro-standardizing data (+++), we present the digitization of a dataset that includes phonological reconstructions. By representing this kind of data in CLDF, we can apply a variety of computer-assisted methods to assess the quality of the reconstructions.

## Background

With the rise of new computational methods (+++) such as trimming (+++), annotation tools (Edictor, LexiData), and software for working with standardized data (lingpy, lingrex), the possibility for working with digital data in historical linguistics has hugely increased. Yet, few datasets that involve reconstructions are openly available in a machine-readable format. For example, only 6 out of the XXX datasets in the current release of Lexibank include reconstructions of proto-languages, and they are quite small datasets. Only one dataset (yanglalo, XXX) features more than 350 concepts, and only two datasets (sidwellvietic XXX, luangthongkumkaren XXX) feature more than 10 language varieties. All six datasets have expert cognate judgements, but no dataset provides explicit alignments of the cognates. This gap will be filled by our digitization and annotation of the Proto-Panoan data originally published by Oliveira (2014).

The Pano language family is spoken in the Amazon lowlands of Peru, Bolivia, and Brasil. It comprises 38 languages (glottolog), which are spoken by an estimated ~41.000 speakers (data from Wikipedia, original behind the ethnologue paywall). A first detailed reconstruction was presented by Shell (xxx), which, however, featured only sparse data for one of the primary branches. Based on data from new documentation projects as well as his own fieldwork, Oliveira (2014) published an advanced reconstruction of Panoan. Through the standardized rework of this dataset, we aim at presenting an example case of sharing data in linguistics that involves reconstructions and explicit alignments of the data. The dataset includes 517 reconstructions for 466 different concepts.

## Workflow: From PDF to CLDF

Following the steps from [List (2021)](https://calc.hypotheses.org/2954) for the linking of a dataset into the CLDF formats, we started by setting up the repository on GitHub where our dataset would be stored.
In this repo, we created and added all the necessary files for the CLDF conversion, generating first the file with the sources in BibTeX formats and placing it in the raw folder ([raw/sources.bib](https://github.com/pano-tacanan-history/oliveiraprotopanoan/blob/main/raw/sources.bib)). 
This file contained all the references listed for the collection of the data in Oliveira's (2014). 
Next, we took care of the files that go in the main folder.
We adjust, firstly, the [setup.py](https://github.com/pano-tacanan-history/oliveiraprotopanoan/blob/main/setup.py) and [metadata.json](https://github.com/pano-tacanan-history/oliveiraprotopanoan/blob/main/metadata.json) files from a CLDF dataset, it can be any, filling them with our dataset specifications.
Afterwards, we added the [CC-By-4.0](https://github.com/pano-tacanan-history/oliveiraprotopanoan/blob/main/LICENSE) license and the [CONTRIBUTORS.md](https://github.com/pano-tacanan-history/oliveiraprotopanoan/blob/main/CONTRIBUTORS.md) file. 
In the MarkDown file, we indicated our names and GitHub usernames as those responsible for the CLDF conversion, as well as Oliveira as the main author.

Afterwards, we handled the data.

+++something about from pdf to raw data+++




The first problem we had to deal with was that, during the extraction of the data in the PDF file, some non-ASCII characters weren't recognized and properly extracted on the raw data file. 
We had to broken down the solution into three tasks in order to tackle the problem and recover the missing characters in the data.
The first one was to parse all the unknown characters into a table with ID and form.
For this task, we wrote a small [raw/parse/archive/parsing.py](https://github.com/pano-tacanan-history/oliveiraprotopanoan/blob/main/raw/parse/archive/parsing.py) Python script that looks like the following:

    from collections import defaultdict

    def parse_line(number, text, ddct):
        for i, char in enumerate(text):
            if char not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,>:-’“.”+/éçãâàôõúë={}*'<>~ê?óñ[]íÁÂüá();‘!":
                ddct[char] += [(number, text[i-5:i + 30])]

This code snippet defines a function called `parse_line` that iterates over each character in the `text` string using the `enumerate` function. 
The third line checks is absent in the given string of allowed character set. 
If the character is not allowed, a tuple containing the `number` and a substring of the `text` is appended to a list associated with the character in the `ddct` dictionary.
This consists of 30 characters, starting from 5 characters before the current character `text[i-5:i+30]` and ending at the current character.

    ddct = defaultdict(list)
    text = open('raw_oliveira.txt', 'r', encoding="utf8").read()
    text = text.split("\n")
    for l in text:
        start = l.split(".")[0]
        parse_line(start, l, ddct)
The last part of the code simply opens the file with the original `raw data` ([raw/parse/archive/raw_oliveira.txt](https://github.com/pano-tacanan-history/oliveiraprotopanoan/blob/main/raw/parse/archive/raw_oliveira.txt)), applies `parse_line` to each line, and prints the collected information sorted by the frequency of occurrence. 
The second and third line of the code open the file on read mode, read its contents into the `text` variable, and split this variable into a list of lines.
The fourth, fifth, and sixth lines create a `for` loop that iterates over each line in the `text` list, split the line by the period, assign the first part to the `start` variable, and called `parse_line` with the `start` (the starting part of the line), `l` (the lines that need to be processed by the function), and `ddct` (where the parsed information is stored) arguments updating the `ddct` dictionary.

Finally, after processing all the lines, the new `for` loop, on the following lines, iterates over the items in `dict`, sorting them by length in descending order. The last line prints the key, its code point, its corresponding line number, and the substring of the line where the key was located.

    for k, v in sorted(ddct.items(), key=lambda x: len(x[1]), reverse=True):
        print(k, "\t", hex(ord(k)), "\t", v[0][0], "\t", v[0][1])
The output of this script was the table with ID and form of all unknown characters. 
With this result, we continue with the second task, namely to create a replacement table for all unknown characters.
This table can be found in [raw/parse/replacements.tsv](https://github.com/pano-tacanan-history/oliveiraprotopanoan/blob/main/raw/parse/replacements.tsv).
To get an impression, the first rows from the table look like the following:

| CHAR    | REPLACEMENT |
|---------|-------------|
| \uf0e9  | ɨ           |
| \uf0a7  | ʂ           |
| \uf053  | ʃ           |
| \uf022  | ˈ           |
| \uf042  | β           |
| 	\uf046 | ɸ           |
| \uf026  | ̃           |
| \uf021  | ́           |
| \uf07c  | ɾ           |
|   \uf0da      |     	́        |


We noticed that there where some extracted concepts that weren't clear as well.
We have some as the following examples: 
`com, empossede` instead of `com, em posse de`, `esp. deplanta` instead of `esp. de planta`, `seguir llevando en los brazos (provavelmente uma reduplicação do verbo em 18.)` instead of `seguir llevando en los brazos`, or `esp. de árvore e também seu fruto (segundo SHELL (1975 [1965]), seria o Zapote)` instead of `esp. de árvore e também seu fruto`.
The same happened with some sources:
`ANONBY2010` instead of `Anonby2010`, `CHÁVEZ2012` instead of `Sparing2012`, `MELATTI1975[2005]` instead of `Melatti2005`, or `	VALENZUELA2003;LORIOT;DAY1993` instead of `	Valenzuela2003;Loriot1993`.
So, we created a replacement table for concepts ([raw/parse/concept_replacements.tsv](https://github.com/pano-tacanan-history/oliveiraprotopanoan/blob/main/raw/parse/concept_replacements.tsv)) and a replacement table for sources ([raw/parse/source_replacements.tsv](https://github.com/pano-tacanan-history/oliveiraprotopanoan/blob/main/raw/parse/source_replacements.tsv)).




The last step was to apply all these replacement tables to the data in order to get the best-possible text.
At this point, however, the text contained still unparseable parts, therefore we modified them manually to avoid not working with them.
We wrote a script called [raw/parse/parse.py](https://github.com/pano-tacanan-history/oliveiraprotopanoan/blob/main/raw/parse/parse.py) to help us with the replacements and to print us the bad lines that needed to be manually modified.
For this, we kept the original extracted data as it is, but we continue working on another file, which we named [raw/parse/raw_oliveira-mod.txt](https://github.com/pano-tacanan-history/oliveiraprotopanoan/blob/main/raw/parse/raw_oliveira-mod.txt)
With the first part of the code, we load the unknown characters replacement table and apply it to the data:
    
    with open("replacements.tsv", encoding="utf8") as f:
    rep = {}
    for line in f.readlines():
        a, b = line.split("\t")
        if a != "CHAR":
            rep[eval('"'+a+'"')] = b.strip()
We do the same with the concepts and sources replacement tables:

    concept_replace = {}
    with UnicodeDictReader("concept_replacements.tsv", delimiter='\t') as reader:
        for line in reader:
            concept_replace[line["OLD"]] = line["NEW"]

    source_replace = {}
    with UnicodeDictReader("source_replacements.tsv", delimiter='\t') as reader:
        for line in reader:
            # print(line)
            source_replace[line["OLD"]] = line["NEW"]


Then, we loaded the data and fragment them into lists of information we needed:

    with open("raw_oliveira-mod.txt", encoding="utf-8") as f:
        data = OrderedDict()
        additional_comments = []
        for line in f:
            line = "".join([rep.get(c, c) for c in line])
            # get first parts with indices
            idx, rest = line[:line.index(".")], line[line.index(".")+1:].strip()
Since the script have comments to understand it, we believe it is very straightforward and could be easily verified with a `print` statement. 
So we will go over it briefly.
We put an exclamation sign at the beginning of some rows with extracted comments or to signal difficult lines to work with.
This lines are ignored in lines `50-52` of the script.
For the rest of the chunk, we separate the `protoform` and `protoconcept` from the `rest`, using `:` as a separator, in lines `54-56`.
Through lines `59-74`, we identified `protoform` from `protoconcept` using `‘` and `’`, we recover the last declared concept if there isn't a `proto-concept`, and we assign the value of uncertainty.
The following big part of the code splits the rest with regexes to get individual entries for each doculect in the data.
The result of this can be seen on the lists assigned to `data[oid]` in lines `213-228`.
The next part of the code gives us the bad lines that we needed to modified manually:

    print("# Found {0} lines without spaces\n".format(len(bad_lines)))
    print("Number | Line\n--- | ---")
    for i, line in enumerate(bad_lines):
        print("{0:5} | {1}".format(i+1, line))
    print("")
    print("# Found {0} entries with individual problematic entries\n".format(
        len(bad_entries)))
    print("Number | Line ID | Entry\n--- | --- | ---")
    for i, (a, b) in enumerate(bad_entries):
        print("{0} | {1:20} | {2}".format(i+1, a, b))
The manual editing process was the only way to obtain a correct parsing, since the text's errors could not be handled otherwise.
Finally, once all the problematic entries were fixed, with the last part of the script, we wrote the new raw file [parsed-entries2.tsv](https://github.com/pano-tacanan-history/oliveiraprotopanoan/blob/main/raw/old_lexibank/parsed-entries2.tsv).
To get the concepts of this data, we wrote a small script [get_concepts.py](https://github.com/pano-tacanan-history/oliveiraprotopanoan/blob/main/raw/old_lexibank/get_concepts.py), where we gather the `proto-concepts` and `other_concepts` as the ones from the doculects.
With this files and the ones in our repo, we could write a first [lexibank script](https://github.com/pano-tacanan-history/oliveiraprotopanoan/blob/main/raw/old_lexibank/lexibank_oliveiraprotopanoan.py) for the CLDF conversion.
The procedure here and the code is to a great extent similar to the ones in the blogpost mention at the beginning of the tutorial, so we won't go any further with this topic here.

+++something about why new raw data+++
The output of this procedure is the file [raw/raw.tsv](https://github.com/pano-tacanan-history/oliveiraprotopanoan/blob/main/raw/raw.tsv). 
This is final version of the polished data employed during the CLDF conversion.



In order to upload the data to Edictor (+++), the software with which we annotate and align the data, we convert the CLDF dataset to a SQLite database. The final dataset includes data from 16 languages with a coverage of more than 60%. In total, the dataset includes 7,307 lexemes, of which 292 lexemes have been tagged as singletons due to uncertain cognacy.

## Annotating the data in Edictor

### Morpheme segmentation

The first step in Edictor consists of preparing the alignments for all words in a cognate set. This involves the flagging of non-cognate material which is present in individual languages, and that is not reconstructed for the proto-language, such as derivational morphemes. While for some cognate sets this is not necessary, other sets have quite complex morphology involved. Preparing those alignments takes time, but sets up the database for high-quality inferences of correspondence patterns. We present an example of this trimming of alignment sites in Figure X.

Figure X: Removing non-cognate material for BIG.

### Uncertainty of reconstructions

The original author incorporated uncertainty in his reconstructions in two exemplary ways. First, he tagged word forms explicitly if he had doubts about the cognacy of those lexemes. In order to infer the best sound correspondence patterns possible from this data, we excluded all those words from the respective cognate set and tagged them as singleton. As Oliveira's reconstruction is partially based on previous reconstructions established by Shell (+++), this tagging provides a critical reassessment of that earlier data. Second, he tagged as uncertain the segmental quality of certain reconstructed phones, for which one or two crucial languages do not have known reflexes. We can search for those cases explicitly in Edictor, making use of the search function. A computer-assisted check of those phones can provide a valuable starting point for further analysis and to check the systematicity of those uncertainty judgements.

## Computational analysis of reconstructions

We can use the aligned data to perform a variety of computational checks, of which we will present one exemplary case. In a preprocessing step, singletons and multiple (292) and multiple entries per language/concept have been removed. Using the regularity-measures of Blum & List (2023+++) that are part of lingrex (+++), we find that of the 735 inferred correspondence patterns, 318 occur at least twice over the dataset. This means that 417 patterns occur only once, making them a problematic case for the regularity of sound change. A closer investigation of those patterns will show whether they are due to erroneous alignments, or due to errors and sporadic sound changes in the data. For the word level, we count how many of the patterns in the cognate set are considered to be recurring, and establish a regularity threshold at 70%. From the 6128 remaining words, 4517 are above this threshold, and 1611 are considered to be irregular. 168 words are even below a threshold of 30%. Those cases should be investigated to see whether erroneous cognate judgements are part of the dataset. A visual comparison of the results applying different regularity threshold is presented in Figure X.

There are several interesting observations about this. First, around half of the entries are fully explainable with correspondence patterns that occur at least twice. Second, At a word-threshold of about 50%, a considerable drop-off in the proportion of regular words can be observed. Third, the differences between a pattern-threshold of 3 and a pattern-threshold of 4 is small. If a pattern occurs at least three times, the chances are high it will recurr more often as well. The difference to correspondence patterns occurring only twice is considerable, however. Based on those very preliminary results, we might propose that a threshold of three is more stable than a lower threshold.

## Conclusion and outlook

We show how the digitization of a dataset from historical linguistics can offer new tools and perspectives on the computer-assisted comparison of phonological reconstructions. By adding explicit alignments of the data and removing non-cognate material, we arrive at high scores of regularity. By identifying patterns and cognate sets that are below certain regularity threshold, we can single out cases which should be analyzed more thoroughly. In the future, we will work on additional methods that help idenfitying problematic patterns and cognate sets, to provide a quantitative assessment of proto-language reconstructions. At the same time, we call for more researchers to share their data in machine-readable files. This step would ensure that historical linguistics heads towards the reproducibility and replicability of the results in the field.
