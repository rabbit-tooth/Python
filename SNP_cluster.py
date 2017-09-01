#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author by 2017/8/30                                    SNP cluster(100%)

import os,re

def getPrefix(str):
    fileName = str.split(".")
    return fileName[0]                                  #prefer python
def getPositionHash(str):
    dist = {}
    posn = open(str,"r+")
    for line in posn:
        dstc = line.split(",")
        dist[dstc[0]] = dstc[2]
    return dist                                         #intelligence nearest principle

fileList = os.listdir("data")
#'''
binId = 0
dict = {}
dist = getPositionHash("data/P.txt")
for f in fileList:
    if re.search("csv",f):                              #find target file
        prefix = getPrefix(f)
    else:
        continue
    inp = open("data/"+f,"r+")
    out = open("data/"+prefix+"_bin.csv","w")

    i = 1
    for line in inp:                                    #reserve ln
        if(i==1):                                       #title
            i += 1
            continue
        line = line.replace(",", "_", 1)
        snp = line.split("_")
        if dict.has_key(snp[1]):
            out.write(snp[0]+","+str(dict[snp[1]])+","+dist[snp[0]])
        else:
            binId += 1
            dict[snp[1]] = binId
            out.write(snp[0]+","+str(binId)+","+dist[snp[0]])
'''
for f in fileList:                                      #Part2_binNum_interval5M sorting before this
    if re.search("_bin.csv",f):
        prefix = getPrefix(f)
    else:
        continue
    inp = open("data/"+f,"r+")
    out = open("data/"+prefix+"_sort.csv","w")
    out.write("snp,binID,binNum,postion\n")

    binID = ""
    flag = 1                                            #default in interval
    for line in inp:
        line = line.replace("\r\n","")
        line = line.replace("\n","")
        bin = line.split(",")

        if bin[1]!=binID:                                #new bin
            if flag==0:
                out.write(preSta)
            flag = 0
            binID = bin[1]
            binNum = 1
            stt = int(bin[2])                                #for interval
            preSta = bin[0]+","+bin[1]+","+str(binNum)+","+bin[2]+"\n"
        else:
            if flag==1:                                 #if beyond, omiit later
                continue
            binNum += 1
            interval = int(bin[2]) - stt
            if interval>5000000:                        #if beyond interval
                flag = 1
            else:
                preSta += bin[0]+","+bin[1]+","+str(binNum)+","+bin[2]+"\n"
    if flag==0:                                         #last bin
        out.write(preSta)
#'''