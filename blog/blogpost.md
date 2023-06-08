# Digitizing Proto-Pano

## Introduction

Data in historical linguistics is typically presented in non-machine-readable formats, such as text-based supplementary material or even handwritten manuscripts. Many annotations and important facts are even given in prose, or remain within the linguists head. Those problems make it difficult for non-experts in the specific field to understand the data, and to reproduce and replicate the results, and also limits the exposure the hard work of the linguist gets. Similar to previous blogposts on retro-standardizing data (+++), we present the digitization of a dataset that includes phonological reconstructions. By representing this kind of data in CLDF, we can apply a variety of computer-assisted methods to assess the quality of the reconstructions.

## Background

With the rise of new computational methods (+++) such as trimming (+++), annotation tools (Edictor, LexiData), and software for working with standardized data (lingpy, lingrex), the possibility for working with digital data in historical linguistics has hugely increased. Yet, few datasets that involve reconstructions are openly available in a machine-readable format. For example, only 6 out of the XXX datasets in the current release of Lexibank include reconstructions of proto-languages, and they are quite small datasets. Only one dataset (yanglalo, XXX) features more than 350 concepts, and only two datasets (sidwellvietic XXX, luangthongkumkaren XXX) feature more than 10 language varieties. All six datasets have expert cognate judgements, but no dataset provides explicit alignments of the cognates. This gap will be filled by our digitization and annotation of the Proto-Panoan data originally published by Oliveira (2014).

The Pano language family is spoken in the Amazon lowlands of Peru, Bolivia, and Brasil. It comprises 38 languages (glottolog), which are spoken by an estimated ~41.000 speakers (data from Wikipedia, original behind the ethnologue paywall). A first detailed reconstruction was presented by Shell (xxx), which, however, featured only sparse data for one of the primary branches. Based on data from new documentation projects as well as his own fieldwork, Oliveira (2014) published an advanced reconstruction of Panoan. Through the standardized rework of this dataset, we aim at presenting an example case of sharing data in linguistics that involves reconstructions and explicit alignments of the data. The dataset includes 517 reconstructions for 466 different concepts.

## Workflow: From PDF to CLDF

+++carlos+++ (nueve de junio)

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
