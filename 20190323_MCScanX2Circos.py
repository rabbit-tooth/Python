#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author by 2019/01/22                           Convert MCScanX collinearity to Circos links

import sys,re

bed = open(sys.argv[1],"r")                     #chr\tstt\tend\tgene
coly = open(sys.argv[2],"r")
out = open(sys.argv[3],"w")

dict = {}
link = 0

for line in bed:
    line = line.rstrip()
    list = line.rsplit("\t", 1)
    dict[list[1]] = list[0]

for line in coly:
    if re.search("#", line, flags=0):
        continue

    list = line.split("\t", 1)
    list = list[1].split()
    if dict.has_key(list[0]) and dict.has_key(list[1]):
        link += 1
        out.write(str(link)+"\t"+dict[list[0]]+"\n")
        out.write(str(link)+"\t"+dict[list[1]]+"\n")
    else:
        print list[0]+","+list[1]+" not in bed"

bed.close()
coly.close()
out.close()