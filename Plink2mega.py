#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author by 2017/9/13                                plink_nosex_mibs for mega

ob = "kin"

def getNosex(filePath):
    i = 0                                           #individual amount
    name = ""
    inp = open(filePath,"r+")
    for line in inp:
        i += 1
        name += "#" + line.split()[0] + "\n"
    name += "," + str(i)
    return name                                     #return String

def getMatrix(filePath):
    dist = "\t"
    inp = open(filePath,"r+")
    for line in inp:
        list = line.split()                         #this step can remove \n
        for distance in list:
            if distance=="1":
                dist += "\n"
                break
            else:
                dist += "\t" + distance
    return dist

name = getNosex(ob+".nosex")
indNum = name.split(",")[1]
matrix = getMatrix(ob+".mibs")

out = open(ob+".meg","w")
out.write("#mega\n!TITLE\tPhylogenetic;\n!Format\tDataType=distance NTaxa="
          +indNum+";\n!Description\tPhylogenetic;\n"+name.split(",")[0]+matrix)