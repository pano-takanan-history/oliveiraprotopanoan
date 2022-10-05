from collections import defaultdict


def blocking(number, text, ddct):
    for concept, line in enumerate(text):
        line.split(":")
        for lang in line:
            ddct[lang] = []

ddct = defaultdict(list)
text = open('raw_oliveira.txt', 'r', encoding="utf8").read()
text = text.split("\n")
for l in text:
    start = l.split(".")[0]
    blocking(start, l, ddct)


def parse(doc):
    for line in doc:
        concept_entries = []
        line_list = line.split(":")
        print(line_list)
        for entry in line_list:
            print(entry)
            concept_entries.append(entry)
        print(concept_entries)


parse(text)



#text = open('raw_oliveira.txt', 'r', encoding="utf8").read()
#for l in text:
    #start = l.split(":")[0]
#print(start)
