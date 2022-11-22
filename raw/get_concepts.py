import csv
from lingpy import Wordlist
from pysem.glosses import to_concepticon

wl = Wordlist("parsed-entries2.tsv")

other_concepts = [[
    "NUMBER",
    "PROTO_ID",
    "GLOSS",
    "PROTO_CONCEPT"
    ]]

with open("../etc/proto_concepts.tsv", "w", encoding="utf8") as f:
    f.write("NUMBER\tPROTO_ID\tGLOSS\tCONCEPTICON_ID\tCONCEPTICON_GLOSS\n")

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

            f.write(f"{i+1}\t{ID}\t{concept}\t{cid}\t{cgl}\n")

        # Other concepts
        else:
            pc = wl[i, "protoconcept"]
            other_concepts.append([
                i+1, ID, concept, pc
            ])

with open("../etc/other_concepts.tsv", "w", encoding="utf8") as file:
    writer = csv.writer(file, delimiter="\t")
    writer.writerows(other_concepts)
