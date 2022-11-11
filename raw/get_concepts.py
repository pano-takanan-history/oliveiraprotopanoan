from lingpy import *
from pysem.glosses import to_concepticon

wl = Wordlist("parsed-entries.tsv")

with open("../etc/concepts.tsv", "w") as f:
    f.write("NUMER\tSPANISH\tCONCEPTICON_ID\tCONCEPTICON_GLOSS\n")
    for i, concept in enumerate(wl.concepts):
        mapped = to_concepticon([{"gloss": concept}], language="es")
        if mapped[concept]:
            cid, cgl = mapped[concept][0][:2]
        else:
            cid, cgl = "", ""
        f.write("{0}\t{1}\t{2}\t{3}\n".format(i+1, concept, cid, cgl))
