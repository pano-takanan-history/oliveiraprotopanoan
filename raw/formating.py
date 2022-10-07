from collections import defaultdict


def block(number, text, ddct):
    #print(text)
    concept_entries = []
    line_list = text.split(":")
    #print(line_list)
    for entry in line_list:
        #print(entry)
        concept_entries.append(entry)
        header = concept_entries[0]
        for i in concept_entries:
            blocks = zip(header, concept_entries[i])
            print(blocks)



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
