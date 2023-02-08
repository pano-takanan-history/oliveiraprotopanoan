from lingpy import Wordlist, Alignments
from lexibank_oliveiraprotopanoan import Dataset as OPP
from lexibase.lexibase import LexiBase

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
        ("concept_conceptinsource", "concept_in_source"),
        ("uncertaincognacy", "uncertain_cognacy"),
        ("cogid_cognateset_id", "cogid"),
        ("segments", "tokens"),
        ("protoset", "proto_set"),
        ("entryinsource", "entry_in_source")
        )
    )

wl = Alignments(wl, ref="cogid", transcription='tokens')
wl.align(ref="cogid")

lex = LexiBase(wl, dbase="edictor/oliveiraprotopanoan.sqlite3")
lex.create("oliveiraprotopanoan")
wl.output('tsv', filename='edictor/oliveiraprotopanoan')

# wl = Wordlist("analysis/bpt-cogids.tsv")
# nexus = write_nexus(wl, ref='cogids', mode='splitstree', filename='analysis/bpt_auto.nex')
