#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author by 2019/11/25            Compute GC content in bed(half interval)

import sys
from Bio import SeqIO
from Bio.SeqUtils import GC

bin = int(sys.argv[2])
out = open(sys.argv[3], "w")

def computeGC(seqName, seqBase, bin):
    lnth = len(seqBase)
    num = lnth // bin
    rmdr = lnth % bin
    buffer = ""
    end = 0

    for i in range(num):
        start = end
        end += bin
        base = seqBase[start:end]
        #base = base.upper()
        #content = (base.count("G")+base.count("C")) / float(bin) * 100
        content = GC(base)
        buffer += seqName + "\t%i\t%i\t%0.1f\n"%(start,end,content)
    if rmdr!=0:
        base = seqBase[end:lnth]
        #base = base.upper()
        #content = (base.count("G")+base.count("C")) / float(lnth-end) * 100
        content = GC(base)
        buffer += seqName + "\t%i\t%i\t%0.1f\n"%(end,lnth,content)
    return buffer

for rec in SeqIO.parse(sys.argv[1], "fasta"):
    buffer = computeGC(rec.id, rec.seq, bin)
    out.write(buffer)

out.close()