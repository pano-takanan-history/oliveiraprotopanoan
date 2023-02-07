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
        "concept_conceptinsource",
        "segments",
        "form",
        "variants",
        "comment",
        "source",
        "cogid_cognateset_id",
        "uncertaincognacy",
        "protoset",
        "entryinsource"
        ),
    # a list of tuples of source and target
    namespace=(
        ("language_id", "doculect"),
        ("concept_name", "concept"),
        ("concept_conceptinsource", "concept in source"),
        ("uncertaincognacy", "uncertain cognacy"),
        ("entryinsource", "entry in source"),
        ("cogid_cognateset_id", "cogid"),
        ("segments", "tokens")
        )
    )

wl = Alignments(wl, ref="cogid", transcription='tokens')
wl.align(ref="cogid")

wl.output('tsv', filename='edictor/oliveiraprotopanoan')

# wl = Wordlist("analysis/bpt-cogids.tsv")
# nexus = write_nexus(wl, ref='cogids', mode='splitstree', filename='analysis/bpt_auto.nex')
