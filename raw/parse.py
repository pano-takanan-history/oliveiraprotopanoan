import re
from collections import OrderedDict


with open("replacements.txt") as f:
    rep = {}
    for line in f.readlines():
        a, b = line.split("\t")
        if a != "CHAR":
            rep[eval('"'+a+'"')] = b.strip()

with open("../etc/languages.tsv") as f:
    langs = {}
    for row in f:
        ents = row.split("\t")
        langs[ents[1]] = ents[0]

# load the data
bad_lines = []
bad_entries = []
oid = 1
with open("raw_oliveira-mod.txt") as f:
    data = OrderedDict()
    for line in f:
        line = "".join([rep.get(c, c) for c in line])
        # get first parts with indices
        idx, rest = line[:line.index(".")], line[line.index(".")+1:].strip()
        
        # we ignore lines that are difficult (two so far)
        if idx.startswith("!"):
            pass
        else:
            # start by separating proto-forms
            proto, rest = rest[:line.index(" : ")-3].strip(), rest[rest.index(" : ")+3:]

            # proto-form and cocept
            if "‘" in proto:
                pform, pconcept = proto.strip()[:-1].split("‘")
                pconcept = pconcept.strip().strip("’")
                pform = pform.strip()
                if ":" in pconcept:
                    bad_lines += [idx]
            else:
                # take concept declared previously
                pform = proto.strip()
            print(idx, pform, pconcept)
            # split entries now to get individual entries here with regexes
            for entry in rest.split(" : "):
                if (":" in entry and not "::" in entry) or not " " in entry:
                    bad_entries += [(idx, entry)]
                else:
                    entry = entry.replace("::", ":")
                    bad_entry = False
                    language = entry[:entry.index(" ")]
                    if language in langs:
                        erest = entry[entry.index(" "):].strip()
                        if "," in erest:
                            erests = [x.strip() for x in erest.split(",")]
                        else:
                            erests = [erest]
                        for erest in erests:
                            erest = erest.replace(";;", ",")
                            if "‘" in erest:
                                try:
                                    form, concept = erest.split("‘")
                                    form = form.strip()
                                    if concept.endswith("’"):
                                        concept = concept[:-1]
                                        note = ""
                                    else:
                                        if "’" in concept:
                                            note = concept.split("’")[1]
                                        else:
                                            note = ""
                                except:
                                    bad_entries += [(idx, entry)]
                                    bad_entry = True
                            else:
                                form = erest
                                concept = "**"+pconcept
                                note = ""
                            if not bad_entry:
                                data[oid] = [idx, langs[language], form, concept,
                                        note, pform,
                                        pconcept, entry]
                                print(idx, language, form, concept)
                                oid += 1
                    else:
                        bad_entries += [(idx, entry)]

                        
print("")

# print out bad lines
print("# Found {0} lines without spaces\n".format(len(bad_lines)))
print("Number | Line\n--- | ---")
for i, line in enumerate(bad_lines):
    print("{0:5} | {1}".format(i+1, line))
print("")
print("# Found {0} entries with individual problematic entries\n".format(
    len(bad_entries)))
print("Number | Line ID | Entry\n--- | --- | ---")
for i, (a, b) in enumerate(bad_entries):
    print("{0} | {1:20} | {2}".format(i+1, a, b))

with open("parsed-entries.tsv", "w") as f:
    for idx, vals in data.items():
        if vals[2].strip() in ["--", "--"] or not vals[2].strip():
            pass
        else:
            f.write(str(idx)+"\t"+"\t".join(vals)+"\n")
        
