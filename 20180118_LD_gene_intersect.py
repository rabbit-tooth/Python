#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author by 2018/01/11                                       LD block intersect with gene domain

import sys

block = open(sys.argv[1],"r")                               #blocks.det
gene = open(sys.argv[2],"r")                                #bedGraph
disb = open(sys.argv[3],"w")                                #csv

LD = []
dict = {}
hash = {}

top = block.readline()
for line in block:                                          #Load LD in array
    list = line.split()
    LD.append(list[1] + "-" + list[2])

for line in gene:                                           #Traverse gene
    list = line.split()

    for i in range(len(LD)):                                #Traverse block
        boundary = LD[i].split("-")

        if int(list[1])>=int(boundary[0]) and int(list[2])<=int(boundary[1]):   #Gene in block
            if dict.has_key(LD[i]):
                dict[LD[i]] = dict[LD[i]] + "\t" + list[3]
            else:
                dict[LD[i]] = list[3]
            break                                           #prefer

        if int(list[1])<int(boundary[0]) and int(list[2])>int(boundary[1]):     #Block in gene
            blockSize = int(boundary[1]) - int(boundary[0])
            if hash.has_key(list[3]):
                bdry = hash[list[3]].split("-")
                if blockSize>bdry[2]:
                    hash[list[3]] = LD[i] + "-" + str(blockSize)
            else:
                hash[list[3]] = LD[i] + "-" + str(blockSize)

        if int(list[1])<int(boundary[0]) and int(list[2])>=int(boundary[0]) and int(list[2])<=int(boundary[1]):
            overlap = int(list[2]) - int(boundary[0])
            if hash.has_key(list[3]):
                bdry = hash[list[3]].split("-")
                if overlap>bdry[2]:
                    hash[list[3]] = LD[i] + "-" + str(overlap)
            else:
                hash[list[3]] = LD[i] + "-" + str(overlap)

        if int(list[1])>=int(boundary[0]) and int(list[1])<=int(boundary[1]) and int(list[2])>int(boundary[1]):
            overlap = int(boundary[1]) - int(list[1])
            if hash.has_key(list[3]):
                bdry = hash[list[3]].split("-")
                if overlap>bdry[2]:
                    hash[list[3]] = LD[i] + "-" + str(overlap)
            else:
                hash[list[3]] = LD[i] + "-" + str(overlap)

for k,v in hash.items():                                    #Induce gene to block
    list = v.split("-")
    section = list[0]+"-"+list[1]
    if dict.has_key(section):
        dict[section] += "\t" + k
    else:
        dict[section] = k

for key,value in dict.items():                              #Output block
    position = key.split("-")
    count = value.split("\t")
    disb.write(position[0]+","+position[1]+","+str(len(count))+"\n")

block.close()
gene.close()