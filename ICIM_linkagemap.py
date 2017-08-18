#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author by 2017/7/2                                            extract linkage map from ICIM sum_file

import os,sys,getopt,re
#opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
#input_file=""
#output_file=""
#for op, value in opts:
#  if op == "-i":
#    input_file = value
#  elif op == "-o":
#    output_file = value
#  elif op == "-h":
#    usage()
#    sys.exit()

file_list = os.listdir("data");
for f in file_list:
    if re.search("txt", f, flags=0):
        component = f.split(".")
        prefix = component[0];
    else:
        continue;

    output = prefix + ".csv";
    icim = open("data/" + f,"r+");
    map = open("data/" + output,"w");
    
    mr = re.compile(r"AX-\d+ +\d+\.\d+ +\d+\.\d+ ");
    map.write("markername,position\n");
    
    for line in icim:
        if re.search("AX-", line, flags=0):
            tup = mr.findall(line),                                  #return a tuple which contains list|tup[0][0] is str
            temp = "".join(tup[0])                                  #return a string|prefer list to str
            temp = temp.strip()
            temp = ",".join(temp.split())
            temp = re.sub(r",\d+\.\d+,", ",", temp, count=0, flags=0)
            temp += "\n"
            map.write(temp)

    icim.close();
    map.close();