# Digitizing Proto-Pano

## Introduction

Historical linguistics has a long tradition of hundreds of pages of manually analyzed data. Papers, books and PhD thesis from that area of study are known for complex data reprentations that run the danger of not being understandable to non-experts in the specific field. This is a serious problem for reproducibility of the results, and also limits the exposure the hard work of the linguistics gets. Based on the reconstruction of Proto-Panoan by Oliveira (+++), we present how such a dataset can be digitized and represented in CLDF, in order to work with a variety of computer-assisted methods that can help. At the same time, we call for researchers to share their data in machine-readable files. This step would ensure that historical linguistics heads towards the reproducibility and replicability of the results in the field.

## Background

The Pano language family is spoken in the Amazon lowlands of Peru, Bolivia, and Brasil. It comprises 38 languages (glottolog), which are spoken by an estimated ~41.000 speakers (data from Wikipedia, original behind the ethnologue paywall). A first detailed reconstruction was presented by Shell (xxx), which, however, featured only sparse data for one of the primary branches. Based on data from new documentation projects as well as his own fieldwork, Oliveira (2014) published an advanced reconstruction of Panoan.

With the rise of new computational methods (+++) such as trimming (+++), annotation tools (Edictor, LexiData), and software for working with standardized data (lingpy, lingrex), the possibility for working with digital data has increased. Yet, few datasets that involve reconstructions are openly available in a machine-readable format. For example, only 6 out of the XXX datasets in the current release of Lexibank include reconstructions of proto-languages, and they are quite small datasets. Only one (yanglalo, XXX) features more than 350 concepts, and only two datasets (sidwellvietic XXX, luangthongkumkaren XXX) feature more than 10 language varieties. All six datasets have expert cognate judgements, but no dataset provides explicit alignments of the cognates. This gap will be filled by our contribution.

Through the digitization and standardization of Oliveira's (2014) reconstruction of Proto-Pano, we aim at presenting an example case of sharing data in linguistics that involves reconstructions and explicit alignments of the data. The dataset includes 517 reconstructions for 466 different concepts. The study includes data from 16 languages with a coverage of more than 60%. In total, the dataset includes 7,307 lexemes, of which 292 lexemes have been tagged as singletons due to uncertain cognacy.

## Workflow: From PDF to CLDF

+++carlos+++ (nueve de junio)

In order to upload the data to Edictor (+++), we convert the CLDF dataset to a SQLite database.

## Annotating the data in Edictor

### Morpheme segmentation

The first step in Edictor then to prepare the alignments for all words in a cognate set. This involves the flagging of non-cognate material, such as morphemes, which is present in individual languages, and that is not reconstructed for the proto-language. While for some cognate sets this is not necessary, other sets have quite complex cases. Preparing those alignments takes time, but sets up the database for high-quality inferences of correspondence patterns. We present an example of this trimming of alignment sites in Figure X.

Figure X: Removing non-cognate material for BIG.

### Uncertainty of reconstructions

The original author incorporated uncertainty in his reconstructions in two exemplary ways. First, he tagged explicitly if he had doubts about the cognacy of some lexemes. As his work is partially based on previous reconstruction established by Shell (+++), his work provides a critical reassessment of the former. In order to infer the best sound correspondence patterns possible from this data, we excluded all those words from the respective cognate set and tagged them as singleton. Second, he tagged as uncertain a couple of phones for which one or two crucial languages do not have known reflexes. A computer-assisted check of those reconstructed phones can provide a good starting point for further analysis and to check the systematicity of those judgements.

## Computational analysis of reconstructions

+++ measure of regularity?+++
