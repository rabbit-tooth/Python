#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author by 2019/03/15                                           Translate CDS into ACID

import sys,re

inp = open(sys.argv[1],"r")
out = open(sys.argv[2],"w")

def trans(cds):
    num = len(cds) // 3
    cds = cds.upper()
    amcd = ""
    for i in range(1,num+1):
        codon = cds[3*(i-1):3*i]
        if dict.has_key(codon):
            amcd += dict[codon]
        else:
            if re.search(r"N", codon, flags=0):                 #Gap
                amcd += "_"
            else:                                               #Throw Exception instead of break
                inp.close()
                out.close()
                sys.exit("No codon "+codon+" !")
    return amcd+"\n"

dict = {"CTA":"L","CTC":"L","CTG":"L","CTT":"L","TTA":"L","TTG":"L",    #Leucine
        "CGA":"R","CGC":"R","CGG":"R","CGT":"R","AGA":"R","AGG":"R",    #Arginine
        "TCA":"S","TCC":"S","TCG":"S","TCT":"S","AGC":"S","AGT":"S",    #Serine
        "ACA":"T","ACC":"T","ACG":"T","ACT":"T",                        #Threonine
        "CCA":"P","CCC":"P","CCG":"P","CCT":"P",                        #Proline
        "GTA":"V","GTC":"V","GTG":"V","GTT":"V",                        #Valine
        "GCA":"A","GCC":"A","GCG":"A","GCT":"A",                        #Alanine
        "GGA":"G","GGC":"G","GGG":"G","GGT":"G",                        #Glycine
        "ATA":"I","ATC":"I","ATT":"I",                                  #Isoleucine
        "AAA":"K","AAG":"K",                                            #Lysine
        "AAC":"N","AAT":"N",                                            #Asparagine
        "CAC":"H","CAT":"H",                                            #Histidine
        "CAA":"Q","CAG":"Q",                                            #Glutamine
        "TAC":"Y","TAT":"Y",                                            #Tyrosine
        "TTC":"F","TTT":"F",                                            #Phenylalanine
        "TGC":"C","TGT":"C",                                            #Cysteine
        "GAC":"D","GAT":"D",                                            #Aspartic Acid
        "GAA":"E","GAG":"E",                                            #Glutamic Acid
        "ATG":"M",                                                      #Methionine
        "TGG":"W",                                                      #Tryptophan
        "TAA":"*","TAG":"*","TGA":"*"}                                  #Stop

top = inp.readline()                                                    #Top Line
out.write(top)
seq = ""

for line in inp:
    if re.search(r">", line, flags=0):
        amcd = trans(seq)
        out.write(amcd+line)
        seq = ""
    else:
        seq += line.rstrip()

amcd = trans(seq)
out.write(amcd)

inp.close()
out.close()