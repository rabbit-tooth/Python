#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author by 2017/7/28                                        recover redundancy from deleted markers|clever

prefix = "7d"
bin = open("data/"+prefix+".sum","r+")
map = open("data/"+prefix+".csv","r+")
out = open("r/"+prefix+".csv","w")
out.write("bin,marker,distance,reserve\n")

def mapDict(linkageMap):                                    #Function obtain effect markers|Args[Handle]
    j = 1
    dictEff = {}                                            #Requires declare
    for marker in linkageMap:
        if j==1:
            j += 1
        else:
            marker = marker.replace("\r\n", "")
            marker = marker.replace("\n", "")
            md = marker.split(",")
            dictEff[md[0]] = md[1]
    return dictEff

i = 1                                                       #top
dictE = mapDict(map)
dictAll = {}
dictBin = {}                                                #Record bin distance
for line in bin:                                            #Load and filt bin info
    if i==1:
        i += 1
    else:
        line = line.replace("\r\n", "")
        line = line.replace("\n", "")
        content = line.split()                              #""empty separator
        if content[5]=="1" or dictE.has_key(content[1]):  #Filt
            info = content[4]+"_"+content[5]
            dictAll[content[1]] = info
            if content[4]!="0" and dictE.has_key(content[1]):#dictE.has_key(content[1]) equals content[5]=="0"
                dictBin[content[4]] = dictE[content[1]]

list = sorted(dictAll.items(),key=lambda item:item[1])      #sorted(iterable,key,reverse)
for tup in list:
    binNum = tup[1].split("_")[0]
    isBin = tup[1].split("_")[1]
    if binNum=="0":                                         #binID==0
        distance = dictE[tup[0]]
    else:
        if isBin=="0":                                      #binID!==0&isBin==0
            distance = dictE[tup[0]]
        else:                                               #binID!==0&isBin==1
            if dictBin.has_key(binNum):
                distance = dictBin[binNum]
                isBin = ""
            else:                                           #Real bin maybe be deleted in linkage map construction
                print tup[0]+" deleted"                     #print has "\n"
                continue
    out.write(binNum+","+tup[0]+","+distance+","+isBin+"\n")

bin.close()
map.close()
out.close()#for k in range(0:)