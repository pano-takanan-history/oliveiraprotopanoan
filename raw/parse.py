import re
from collections import OrderedDict


with open("replacements.txt") as f:
    rep = {}
    for line in f.readlines():
        a, b = line.split("\t")
        if a != "CHAR":
            rep[eval('"'+a+'"')] = b.strip()

# load the data
bad_lines = []
bad_entries = []
with open("raw_oliveira-mod.txt") as f:
    data = OrderedDict()
    for line in f:
        line = "".join([rep.get(c, c) for c in line])
        # get first parts with indices
        idx, rest = line[:line.index(".")], line[line.index("."):].strip()
        
        # we ignore lines that are difficult (two so far)
        if idx.startswith("!"):
            pass
        else:
            # start by separating proto-forms
            proto, rest = rest[:line.index(" : ")].strip(), rest[rest.index(" : ")+3:]

            # proto-form and cocept
            if "‘" in proto:
                pform, pconcept = proto.strip()[:-1].split("‘")
                if ":" in pconcept:
                    bad_lines += [idx]
            else:
                # take concept declared previously
                pform = proto.strip()
            print(idx, pform, pconcept)
            # split entries now to get individual entries here with regexes
            for entry in rest.split(" : "):
                if ":" in entry or not " " in entry:
                    bad_entries += [(idx, entry)]
                else:
                    bad_entry = False
                    language = entry[:entry.index(" ")]
                    erest = entry[entry.index(" "):].strip()
                    if "‘" in erest:
                        try:
                            form, concept = erest.split("‘")
                            form = form.strip()
                            concept = concept.strip()
                        except:
                            bad_entries += [(idx, entry)]
                            bad_entry = True
                    else:
                        form = erest
                        concept = pconcept
                    if not bad_entry:
                        print(idx, language, form, concept)

                    
print("")

# print out bad lines
print("# Found {0} lines without spaces".format(len(bad_lines)))
for i, line in enumerate(bad_lines):
    print("- {0:5} || {1}".format(i+1, line))
print("")
print("# Found {0} entries with individual problematic entries".format(
    len(bad_entries)))
for i, (a, b) in enumerate(bad_entries):
    print("- {0:5} || {1:20} || {2}".format(i+1, a, b))


