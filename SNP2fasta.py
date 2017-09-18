#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author by 2017/9/13                                Convert SNP to fa

def getIndvFa(filePath,indvNum):                    #Obtain a sequence for one individual
    inp = open(filePath,"r+")
    linNum = 0
    for line in inp:
        line = line.replace("\r\n","")
        line = line.replace("\n","")
        list = line.split(",")
        if linNum==0:
            stream = ">" + list[indvNum] + "\n"
            linNum = 1
            continue
        if linNum<=80:
            stream += list[indvNum]
            linNum += 1
        else:
            stream += "\n" + list[indvNum]
            linNum = 2
    stream += "\n"
    return stream

filePath = "HN.csv"
out = open("HN.fasta","w")

with open(filePath, 'r') as top:                    #Obatain indvNum
    CEL = top.readline()
    list = CEL.split(",")
for i in range(3,len(list)):
    fasta = getIndvFa(filePath,i)
    out.write(fasta)