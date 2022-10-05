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





#text = open('raw_oliveira.txt', 'r', encoding="utf8").read()
#for l in text:
    #start = l.split(":")[0]
#print(start)
