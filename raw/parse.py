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
            proto, rest = rest[:line.index(" : ")].strip(), rest[rest.index(" : "):]

            # proto-form and cocept
            if "‘" in proto:
                pform, concept = proto.strip()[:-3].split("‘")
                if ":" in concept:
                    bad_lines += [idx]
            else:
                # take concept declared previously
                pform = proto.strip()

            print(idx, pform, concept)
print("")

# print out bad lines
print("# Found {0} lines without spaces".format(len(bad_lines)))
for line in bad_lines:
    print(line)
