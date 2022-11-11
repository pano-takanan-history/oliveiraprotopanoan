from collections import defaultdict
from lingpy import *
from pysem.glosses import to_concepticon

wl = Wordlist("parsed-entries.tsv")

with open("../etc/concepts.tsv", "w") as f:
    f.write("NUMER\tSPANISH\tCONCEPTICON_ID\tCONCEPTICON_GLOSS\tProto-Concept\n")

    proto_concepts = []
    for i in wl:
        if wl[i, "protoconcept"] not in proto_concepts:
            proto_concepts.append(wl[i, "protoconcept"])

    for i, concept in enumerate(wl.concepts):
        if concept in proto_concepts:
            is_proto = 1
            mapped = to_concepticon([{"gloss": concept}], language="es")

            if mapped[concept]:
                cid, cgl = mapped[concept][0][:2]
        else:
            cid, cgl, is_proto = "", "", ""

        # print(wl.concepts[i])
        f.write("{0}\t{1}\t{2}\t{3}\t{4}\n".format(i+1, concept, cid, cgl, is_proto))
