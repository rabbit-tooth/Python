#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author by 2017/9/15                                Convert VCF to SNP | perfect

inp = open("HN.vcf","r+")
out = open("HN.csv","w")
out.write("SNPID,chr,pos")

linNum = 0
for line in inp:
    list = line.split()
    REF = list[3]
    ALT = list[4]

    if linNum==0:                                   #Top line
        stream = ""
        for i in range(9,len(list)-1):
            stream += "," + list[i]
        stream += "\n"
        out.write(stream)
        linNum = -1
        continue

    stream=list[2]+","+list[0]+","+list[1]          #Ordinary line
    for i in range(9,len(list)-1):
        if list[i]=="0/0":
            stream += "," + REF
        elif list[i]=="1/1":
            stream += "," + ALT
        elif list[i]=="./.":
            stream += ",-"
        else:
            raise Exception(list[2]+" base error!")
    stream += "\n"
    out.write(stream)