#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author by 2019/03/14                                   Convert bed6 to bed12 for bedtools getfasta

import sys

inp = open(sys.argv[1],"r")                             #Sorted col4 col2 bed6
out = open(sys.argv[2],"w")

i = 1
dict = {}                                               #Key <- ct    s,e    s,t

for line in inp:
    list = line.split()
    size = str(int(list[2]) - int(list[1]) + 1)

    if i==1:                                            #Top Line
        chr = list[0]
        head = list[1]
        tail = list[2]
        id = list[3]
        strand = list[5]
        dict[id] = "1\t" + size + "\t0"
        i += 1
        continue

    if dict.has_key(list[3]):
        css = dict[id].split("\t")

        ct = str(int(css[0]) + 1)
        se = css[1] + "," + size
        st_relat = str(int(list[1]) - int(head))
        st = css[2] + "," + st_relat

        tail = list[2]
        dict[list[3]] = ct + "\t" + se + "\t" + st
    else:
        out.write(chr+"\t"+str(int(head)-1)+"\t"+tail+"\t"+id+"\t.\t"+
                  strand+"\t"+str(int(head)-1)+"\t"+tail+"\t0,0,0\t"+dict[id]+"\n")
        chr = list[0]
        head = list[1]
        tail = list[2]
        id = list[3]
        strand = list[5]
        dict[id] = "1\t" + size + "\t0"

out.write(chr+"\t"+str(int(head)-1)+"\t"+tail+"\t"+id+"\t.\t"+
          strand+"\t"+str(int(head)-1)+"\t"+tail+"\t0,0,0\t"+dict[id]+"\n")

inp.close()
out.close()