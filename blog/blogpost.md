# Digitizing Proto-Pano

## Introduction

Historical linguists have a long tradition of reconstructing proto-languages in a long and tedious work of manual comparison of data.

With the rise of new computational methods (+++) such as trimming (+++), annotation tools (Edictor, LexiData), and software for working with standardized data (lingpy, lingrex), the demand for digital data has increased. Yet, few datasets are openly available in a machine-readable format. Papers, books and PhD thesis that reconstruct proto-languages are known for long appendices that run the danger of not being understandable to non-experts in the specific field. This is a serious problem for reproducibility of the results.

+++how large are the datasets that are part of protocore? are we the largest?+++

Through the digitization and standardization of Oliveira's (2014) reconstruction of Proto-Pano, we aim at presenting an example case of sharing data in linguistics that involves reconstructions. At the same time, we call for researchers to share their data in machine-readable files. This step would ensure that historical linguistics towards the reproducibility and replicability of the results in the field.

## Workflow: From PDF to CLDF

+++carlos+++ (nueve de junio)

## Annotation in Edictor

+++frederic+++
In a first step, we align the words in each cognate set. This involves the flagging of non-cognate material, such as morphemes, which is present in individual languages, and that is not reconstructed for the proto-language. We present an example of this trimming of morphemes in Figure X.

+++figure of non-cognate material+++

During this step, we check whether the words that the original author tagged as "uncertain cognacy" fit the pattern, or not. If not, we assign the word a different cognate ID, in order to not mess up the correspondence pattern analysis.

There are other cases where inconsistencies in the data lead to problems.

- check nasals
- check grouping of sounds, e.g. glottal stops

+++ measure of regularity?+++
+++ plot with colex networks of "concept in source" per cogid
