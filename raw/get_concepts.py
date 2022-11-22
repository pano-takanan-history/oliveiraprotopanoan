import csv
from lingpy import Wordlist
from pysem.glosses import to_concepticon

wl = Wordlist("parsed-entries2.tsv")

other_concepts = [[
    "NUMBER",
    "GLOSS",
    "PROTO_ID",
    "PROTO_CONCEPT"
    ]]

with open("../etc/proto_concepts.tsv", "w", encoding="utf8") as f:
    f.write("NUMBER\tGLOSS\tCONCEPTICON_ID\tCONCEPTICON_GLOSS\tPROTO_ID\tPROTO_CONCEPT\n")

    for i in wl:
        ID = wl[i, "IDX"]
        concept = wl[i, "concept"]

        # Proto-Concepts
        if wl[i, "doculect"] == "Proto-Panoan":
            PP = 1
            mapped = to_concepticon([{"gloss": concept}], language="pt")

            if mapped[concept]:
                cid, cgl = mapped[concept][0][:2]
            else:
                cid, cgl = "", ""

            f.write(f"{i+1}\t{concept}\t{cid}\t{cgl}\t{ID}\t{PP}\n")

        # Other concepts
        else:
            PP = 0
            other_concepts.append([
                i+1, concept, ID, PP
            ])

with open("../etc/other_concepts.tsv", "w", encoding="utf8") as file:
    writer = csv.writer(file, delimiter="\t")
    writer.writerows(other_concepts)
