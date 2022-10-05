from collections import defaultdict


def block(number, text, ddct):
    #print(text)
    concept_entries = []
    line_list = text.split(":")
    #print(line_list)
    for entry in line_list:
        #print(entry)
        concept_entries.append(entry)
        print(concept_entries)

ddct = defaultdict(list)
text = open('raw_oliveira.txt', 'r', encoding="utf8").read()
text = text.split("\n")
#print(text)
for l in text:
    start = l.split(".")[0]
    block(start, l, ddct)





# parse(text)



#text = open('raw_oliveira.txt', 'r', encoding="utf8").read()
#for l in text:
    #start = l.split(":")[0]
#print(start)
