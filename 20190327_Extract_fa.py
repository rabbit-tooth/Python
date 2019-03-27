#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author by 2018/12/05                                        Extract fa[sta]

import sys,re
print "Usage: python script.py Fasta List Out"

faa = open(sys.argv[1], "r")
tgt = open(sys.argv[2], "r")
out = open(sys.argv[3], "w")

#Arthm 1
dict = {}

def isTarget(seqHead):
    flag = "N"                                              #Local variable

    seqHead = seqHead.rstrip().replace(">", "")
    if seqHead in dict.keys():                              #Global variable
        flag = "Y"

    return flag

for line in tgt:
    dict[line.rstrip()] = 1

for line in faa:
    if re.search(">", line, flags=0):
        flag = isTarget(line)                               #Global variable 
    if flag=="Y":
        out.write(line)

'''Arthm 2
from Bio import SeqIO

faix = SeqIO.index(sys.argv[1], "fasta")
print str(len(faix))+" records in "+sys.argv[1]+"."
count = 0
total = 0

for line in tgt:
    line = line.rstrip()
    total += 1
    if line in faix:
        record = faix[line]
        SeqIO.write(record, out, "fasta")
        count += 1
    else:
        print line+" Not Exists!"

print str(count)+" of "+str(total)+" records were found in list."
'''

faa.close()
tgt.close()
out.close()