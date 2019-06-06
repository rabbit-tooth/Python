#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author by 2019/06/01                                   After Ontologizer

import os,sys,re

obo = open(sys.argv[1], "r")
rec = open(sys.argv[3], "w")

def loadHash(fileHand):
    hash = {}
    top = fileHand.readline()
    for line in fileHand:
        list = line.rstrip().split("\t")
        hash[list[0]] = list[2]
    return hash

def getDirFiles(dir):                                   #Obtain specific file list in dir
    obj = os.walk(dir)
    list = []
    for tup in obj:
        fileList = tup[2]
    for file in fileList:
        rschOb = re.search(r"^table-(\d+)-.+\.txt$", file, flags=0)
        if rschOb:
            list.append(rschOb.group(0))
    return list

def processFile(file, hash):
    rst = ""
    inp = open(file, "r")
    top = inp.readline()

    for line in inp:
        cols = line.split("\t")
        if float(cols[10])<=0.05:
            if hash.has_key(cols[0]):
                rst += cols[0]+"\t"+cols[1]+"\t"+cols[2]+"\t"+cols[3]+"\t"+cols[4]+"\t"+cols[10]+"\t"+hash[cols[0]]+"\t"+cols[12]
            else:
                rst += cols[0]+"\t"+cols[1]+"\t"+cols[2]+"\t"+cols[3]+"\t"+cols[4]+"\t"+cols[10]+"\tUNKNOWN\t"+cols[12]

    inp.close()
    return rst

dict = loadHash(obo)
list = getDirFiles(sys.argv[2])

for file in list:
    rst = processFile(sys.argv[2]+"/"+file, dict)
    if rst:
        name = file.replace("txt", "rst")
        out = open(name, "w")
        out.write(rst)
        out.close()
    else:
        rec.write(file+"\n")

obo.close()
rec.close()