#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author by 2019/04/08                                    Parse obo

import sys,re

inp = open(sys.argv[1], "r")
out = open(sys.argv[2], "w")

dict = {}
flag = 0
num = 0

for line in inp:
    num += 1
    if re.search(r"^\[Term\]$", line, flags=0):
        if flag==0:                                    #Top valid line
            pass
        elif flag==3:
            dict[id] = name + "\tunknown"
            print "Warning: "+id+" no namespace"
        elif flag==4:
            dict[id] = name + "\t" + nasp
        else:
            sys.exit("Unexpect line "+str(num))
        flag = 1
    elif re.search(r"^id:", line, flags=0):
        if flag==1:
            id = line.split()[1]
            flag = 2
        else:
            sys.exit("Unexpect line "+str(num))
    elif re.search(r"^name:", line, flags=0):
        if flag==2:
            name = line.rstrip().split(": ", 1)[1]
            flag = 3
        else:
            sys.exit("Unexpect line "+str(num))
    elif re.search(r"^namespace:", line, flags=0):
        if flag==3:
            nasp = line.rstrip().split(": ")[1]
            flag = 4
        else:
            sys.exit("Unexpect line "+str(num))
    elif re.search(r"^\[Typedef\]$", line, flags=0):
        break
    else:
        continue

if flag==3:                                             #Last unit
    dict[id] = name + "\tunknown"
    print "Warning: "+id+" no namespace"
elif flag==4:
    dict[id] = name + "\t" + nasp
else:
    print "Warning: Last ontology"

out.write("ID\tNAME\tNASP\n")                           #Output
for k,v in dict.items():
    out.write(k+"\t"+v+"\n")

inp.close()
out.close()