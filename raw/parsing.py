from typing import List
from collections import defaultdict

with open('raw_oliveira.txt', 'r', encoding="utf8") as f:
    for line in f:
        data = line.split()


    def parse_line(number, text, ddct):
        for i, char in enumerate(text):
            if char not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789":
                ddct[char] += [(number, text[i - 5:i + 20])]

        ddct = defaultdict(list)
        text = open(f).read()
        text = text.split("\n")
        for l in text:
            print(text)
            start = l.split(".")[0]
            parse_line(start, l, ddct)
        for k, v in sorted(ddct.items(), key=lambda x: len(x[1]), reverse=True):
            print(k, "\t", hex(chr(k)), "\t", v[0][0], "\t", v[0][1])  # first context observed!)
