#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author by 2018/12/07                                        Extract paralogy from OrthoMCL groups.txt

import sys,re

inp = open(sys.argv[1],"r")
out = open(sys.argv[2],"w")
spc = sys.argv[3]                                           #Target species

def getParalogy(list):
    num = 0
    para = ""
    for i in range(1,len(list)):
        if re.search(r"^"+spc+"\|", list[i], flags=0):      #"^%s\|"%spc
            num += 1
            para += list[i]+"\n"
    if num>=3:
        return para
    else:
        return "N"

for line in inp:
    list = line.split()
    cont = getParalogy(list)

    if cont=="N":
        pass
    else:
        out.write(list[0]+"\n"+cont)

inp.close()
out.close()