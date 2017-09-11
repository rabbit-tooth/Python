#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author by 2017/9/1                                                 #ICIM CMP input format

chr = "1a"
mapNum = "4"

def checkCommonMarkers(h,str):                                      #h:hash
    inp = open(str,"r+")
    i = 1
    common = {}
    for line in inp:
        if i==1:
            i += 1
            continue                                                #prefer Python
        snp = line.split(",")
        if h.has_key(snp[0]):
            common[snp[0]] = 1
    return common
def getMapMarkers(str):                                             #str:file path
    inp = open(str,"r+")
    i = -1
    for line in inp:
        i += 1
    return i                                                        #intelligence
def writeMapDist(str,op,mapID):
    inp = open(str,"r+")
    i = 1
    for line in inp:
        if i==1:
            i += 1
        else:
            snp = line.split(",")
            op.write(snp[0]+"\t"+mapID+"\t"+snp[1])

inp = open(chr+"_ak.csv","r+")                                      #check common markers
i = 1
comm = {}
for line in inp:
    if i==1:
        i += 1
        continue
    snp = line.split(",")
    comm[snp[0]] = 1
comm = checkCommonMarkers(comm,chr+"_xia.csv")
comm = checkCommonMarkers(comm,chr+"_jing.csv")
comm = checkCommonMarkers(comm,chr+"_zhang.csv")
if len(comm) == 0:
    raise Exception("No commom markers!")

out = open(chr+"_integrate.csv","w")                                #output general information
out.write("2\n1\n"+mapNum+"\n\n")

snpNum = getMapMarkers(chr+"_ak.csv")                               #output snpNum in each mapID
out.write("map1\t"+str(snpNum)+"\n")
snpNum = getMapMarkers(chr+"_xia.csv")
out.write("map2\t"+str(snpNum)+"\n")
snpNum = getMapMarkers(chr+"_jing.csv")
out.write("map3\t"+str(snpNum)+"\n")
snpNum = getMapMarkers(chr+"_zhang.csv")
out.write("map4\t"+str(snpNum)+"\n")
out.write("\n")

writeMapDist(chr+"_ak.csv",out,"1")                                 #output SNPs
writeMapDist(chr+"_xia.csv",out,"2")
writeMapDist(chr+"_jing.csv",out,"3")
writeMapDist(chr+"_zhang.csv",out,"4")