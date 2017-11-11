#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author by 2017/11/10                                               obtain sub-pop from admixture.N.Q

import sys,re

idvd = open(sys.argv[1],"r")                                        #VCF
matrixQ = open(sys.argv[2],"r")                                     #Q estimate
subdiv = open(sys.argv[3],"w")

def getPopu(list):                                                  #Filt max Q value and get popu
    max = 0
    popu = 0
    for i in range(len(list)):
        if max<list[i]:                                             #String can be used as number
            max = list[i]
            popu = i + 1
    return str(popu)

top = idvd.readline()                                               #Get individuals
top = re.sub(r"#CHROM.+FORMAT\t","",top)
top = top.rstrip()
inds = top.split("\t")

j = 0
for line in matrixQ:                                                #Select sub_pop for each individual
    line = line.rstrip()
    em = line.split(" ")
    subpop = getPopu(em)

    subdiv.write(inds[j]+","+subpop+"\n")
    j += 1

idvd.close()
matrixQ.close()
subdiv.close()