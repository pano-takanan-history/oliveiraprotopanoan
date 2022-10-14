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
        new_entry1 = " ".join(entry.split(" ")[1:])
        #print(entry.split(" "))
        #print(new_entry1)
        new_entry2 = " ".join(entry.split(" ")[2:])
        #print(new_entry2)
        #if "‘" in new_entry2:
            #print("true:", new_entry2)
            #pass
        #else:
            #print("false:", new_entry2)
        #print("Language: {0} | entry: {1}".format(lng, new_entry))
        #print("Language: {0} | entry: {1}".format(lng, new_entry2))
        concepts = new_entry2[new_entry2.find("‘") + 1:new_entry2.find("’")]
        if not "‘" in new_entry2:
            concepts = ''
        # print(concepts)
        #print(new_entry2)
        for x in new_entry2:
            if x in concepts:
                print(x)
                pass
        if "o" in concepts:
            print("This statement deletes any o you might encounter")
        new_entry3 = [x for x in new_entry2 if x not in concepts]
        forms = "".join(new_entry3)
        # print(forms)
        print("Language: {0} | entry: {1} | concept: {2}".format(lng, forms, concepts))



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
