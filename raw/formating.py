from collections import defaultdict
import re

def block(number, text, ddct):
    #print(text)
    concept_entries = []
    line_list = text.split(":")
    # print(line_list)
    # print(number)
    idf = line_list[0]
    #print(idf)
    rest = line_list[1:]
    #print(rest)
    for entry in rest:
        #print(entry)
        lang = [x for x in entry.split() if x]
        #print(lang)
        lng = lang[0]
        #print(lng)
        new_entry = " ".join(entry.split(" ")[1:])
        #print(new_entry)
        #lang = [x for x in entry.split() if x]
        #print(lang)
        print("Language: {0} | entry: {1}".format(lng, new_entry))



    #entry_list = []

    #for line in line_list:
        #print(line)
    #    if line == idf:
     #       protoform = line.split("‘")[0]
      #      protoform = protoform.split("(")[0]
            #print(protoform)
       #     pass
        #else:
         #   lang = line.split(" ")
            #print(lang)
          #  while ("" in lang):
           #     lang.remove("")
                #print(lang)


            #if "‘" in line:
                #print(line)
        #source = line[line.find("(") + 1:line.find(")")]
        # print(source)
        # if not source:
           # source = ''


        # print(f"{protoform} || {concept} || {source} ")
    #    for entry in line_list:
    #        print(entry)
    #        concept_entries.append(entry)
    #        break


ddct = defaultdict(list)
text = open('raw_oliveira.txt', 'r', encoding="utf8").read()
text = text.split("\n")
#print(text)
for l in text:
    l_splitted = l.split(".")
    start = l_splitted[0]
    final_entry = l_splitted[1:]
    block(start, "".join(final_entry), ddct)

    # break


# parse(text)



#text = open('raw_oliveira.txt', 'r', encoding="utf8").read()
#for l in text:
    #start = l.split(":")[0]
#print(start)
