#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author by 2019/04/25                                Markup gene list for clans

import sys,re

dict = {}
i = 1

def getList(dt):
    rst = ""

    all = open(sys.argv[2], "r")
    for line in all:
        line = line.rstrip()
        if dt.has_key(line):
            rst += line + "\tY\n"
            del dt[line]
        else:
            rst += line + "\tN\n"
    if dt:
        rst = ""
    all.close()

    return rst

cls = open(sys.argv[1], "r")
for line in cls:
    reOb = re.search(r"^group_(\d+):$", line, flags=0)
    if reOb:
        if i==1:
            i += 1
        else:
            dict[name] = clan
        name = reOb.group(1)
        clan = {}
    else:
        line = line.rstrip()
        clan[line] = 1
dict[name] = clan
cls.close()

for k,v in dict.items():
    rst = getList(v)
    if not rst:
        sys.exit(k+" error.")
    out = open(k+".list", "w")
    out.write("gene\tisTarget\n"+rst)
    out.close()