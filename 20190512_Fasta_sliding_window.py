#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author by 2019/05/11                        Split fa[sta] into sliding window

import sys,re
from Bio import SeqIO

winw = int(sys.argv[3])
step = int(sys.argv[4])

with open(sys.argv[2], "w") as out:
    for record in SeqIO.parse(sys.argv[1], "fasta"):
        seq = str(record.seq)
        lnth = len(seq)

        if winw>=lnth:
            if re.search(r"^N+$", seq, flags=0):
                pass
            else:
                out.write(">"+record.id+"\n")
                out.write(seq+"\n")
            continue

        num = (lnth-winw) // step + 1
        for i in range(1, num+1):
            stt = step*(i-1)
            end = step*(i-1) + winw
            slice = seq[stt:end]
            if re.search(r"^N+$", slice, flags=0):
                pass
            else:
                out.write(">"+record.id+"-"+str(i)+"\n")
                out.write(slice+"\n")