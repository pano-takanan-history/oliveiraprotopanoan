# Digitizing Proto-Pano

## Introduction

Historical linguistics has a long tradition of hundreds of pages of manually analyzed data. With the rise of new computational methods (+++) such as trimming (+++), annotation tools (Edictor, LexiData), and software for working with standardized data (lingpy, lingrex), the possibility for working with digital data has increased. Yet, few datasets are openly available in a machine-readable format. Papers, books and PhD thesis that reconstruct proto-languages are known for long appendices that run the danger of not being understandable to non-experts in the specific field. This is a serious problem for reproducibility of the results, and also limits the exposure the hard work of the linguistics gets.

Through the digitization and standardization of Oliveira's (2014) reconstruction of Proto-Pano, we aim at presenting an example case of sharing data in linguistics that involves reconstructions. Within Lexibank (+++), the largest currently available dataset features 1001 concepts reconstructed for Proto-lalo (+++) with data from 8 languages, providing over 8,500 lexemes. The Oliveira (2014) dataset has only 466 concepts, but includes data from 16, arguably more distantly related languages, and thus provides an important contribution to the availability of digitized data for reconstructions. At the same time, we call for researchers to share their data in machine-readable files. This step would ensure that historical linguistics towards the reproducibility and replicability of the results in the field.

## Workflow: From PDF to CLDF

+++carlos+++ (nueve de junio)

## Annotation in Edictor

In order to upload the data to Edictor (+++), we convert the CLDF dataset to a SQLite database. The first step in Edictor is then to prepare the alignments for all words in a cognate set. This involves the flagging of non-cognate material, such as morphemes, which is present in individual languages, and that is not reconstructed for the proto-language. We present an example of this trimming of alignment sites in Figure X.

+++figure of non-cognate material+++

During this step, we check whether the words that the original author tagged as "uncertain cognacy" fit the pattern, or not. If not, we assign the word a different cognate ID, in order to not mess up the correspondence pattern analysis. Next, we tag vowels in a way that accented vowels are treate

+++ do we separate nasals?

## Computational analysis of reconstructions

+++ measure of regularity?+++
+++ plot with colex networks of "concept in source" per cogid
