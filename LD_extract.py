#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author by 2017/7/12                                            extract abstract from SPINEblocks and info

import os,re

file_list = os.listdir("data")
for f in file_list:
    if re.search("info", f, flags=0):
        component = f.split(".")
        prefix = component[0]
    else:
        continue
    info = open("data/"+f,"r+")
    block = open("data/"+prefix+".ped.SPINEblocks","r+")
    output = open("data/"+prefix+".csv","w")
    
    temp = "Block,Snp number,Start snp,Start pos,End snp,End pos,Distance\n"
    output.write(temp)
    
    lt = ["0"]                                                      #Require define
    for line in info:                                               #Load info into array
        line = re.sub("\t", ",", line, count=0, flags=0)
        line = line.replace("\r\n", "")
        line = line.replace("\n", "")
        lt.append(line)                                             #'tuple' object does not support item assignment
    
    i = 1
    for line in block:
        if(re.search("BLOCK", line, flags=0)):                      #invention
            bk = line.split(".")
            bk[1] = re.sub("  MARKERS: ", "", bk[1], count=0, flags=0)
            marker = bk[1].split()
            sn = int(marker[len(marker)-1]) - int(marker[0]) + 1    #snp number    len from 1
            ss = lt[int(marker[0])]                                 #start snp
            ed = lt[int(marker[len(marker)-1])]                     #end snp
            distance = int(ed.split(",")[1]) - int(ss.split(",")[1])
            temp = bk[0] + "," + str(sn) + "," + ss + "," + ed + "," + str(distance) + "\n"
            output.write(temp)
        else:                                                       #!:||
            pass
        i += 1                                                      #!:i++
    
    info.close()
    block.close()
    output.close()