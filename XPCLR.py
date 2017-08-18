#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author by 2017/7/27                                                Process XPCLR block

if __name__ == '__main__':
    import sys,string
    print sys.argv[0]

xpclr = open("data/P0-CLR-CL-top5.csv","r+")
block = open("data/P0.csv","w")
#with open("csv", 'r') as xpclr:                                    only read top line
#    top = xpclr.readline()

chr = 0                                                             #chromosome
cor = 0                                                             #correlation
i = 0                                                               #top
for line in xpclr:
    line = line.replace("\r\n", "")
    line = line.replace("\n", "")
    if i==0:
        block.write(line+",chr,start,end\n")
        i += 1
        continue
    content = line.split(",")
    
    if chr!=content[0]:                                             #new chr    use int as str in once
        chr = content[0]
        start = content[1]
        block.write(line+"\n")
        if string.atof(content[4])>1:
            cor = 0
        else:
            cor = 1
        continue                                                    #prefer python
    
    if cor==0:                                                      #|or new block
        chr = content[0]
        start = content[1]
        block.write(line+"\n")
        if string.atof(content[4])>1:
            cor = 0
        else:
            cor = 1
        continue
    
    if cor==1:                                                      #in one block
        if string.atof(content[4])<=1:                              #strict [0,1]:!&    if last of chr is [0,1] tend output more complex
            block.write(line+"\n")
        else:
            block.write(line+","+chr+","+start+","+content[1]+"\n")
            cor = 0

xpclr.close()
block.close()