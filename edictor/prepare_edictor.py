from lingpy import Wordlist, Alignments
from lexibank_oliveiraprotopanoan import Dataset as OPP

# load the wordlist
ds = OPP()

wl = Wordlist.from_cldf(
    str(ds.cldf_dir.joinpath("cldf-metadata.json").as_posix()),
    # columns to be loaded from CLDF set
    columns=(
        "language_id",
        "concept_name",
        "concept_concepticon_gloss",
        "segments",
        "form",
        "variants",
        "comment",
        "source",
        "cognacy",
        "concept_from_proto",
        "entryinsource",
        "paragraph"
        ),
    # a list of tuples of source and target
    namespace=(
        ("language_id", "doculect"),
        ("concept_concepticon_gloss", "concept"),
        ("concept_name", "concept_in_source")
        )
    )


wl.output('tsv', filename='edictor/oliveiraprotopanoan')

# wl = Wordlist("analysis/bpt-cogids.tsv")
# nexus = write_nexus(wl, ref='cogids', mode='splitstree', filename='analysis/bpt_auto.nex')
