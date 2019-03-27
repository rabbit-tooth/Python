#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author by 2019/03/25                                   Format MCSCanX tandem

import sys,re

tdm = open(sys.argv[1], "r")
out = open(sys.argv[2], "w")

dict = {}
i = 0

def getTandem(gene, dictionary):
    for k,v in dictionary.items():
        if re.search(r"%s,"%gene, v, flags=0):
            return k
    return "N"

for line in tdm:
    line = line.rstrip()
    list = line.split(",")
    m = getTandem(list[0], dict)
    n = getTandem(list[1], dict)

    if m=="N" and n=="N":
        i += 1
        dict[i] = line + ","
    if m!="N" and n=="N":
        dict[m] += list[1] + ","
    if m=="N" and n!="N":
        dict[n] += list[0] + ","
    if m!="N" and n!="N":
        if m==n:                                        #Check exception
            print line
        else:
            unit = dict[m] + dict[n]
            dict[m] = unit
            del dict[n]

for val in dict.values():
    val = re.sub(r",$", "\n", val, count=0, flags=0)
    out.write(val)

tdm.close()
out.close()