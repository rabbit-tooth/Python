#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Author by 2019/06/27                    Kmeans cluster for vectors

import sys,numpy
from scipy.cluster.vq import whiten,kmeans,vq
from sklearn.cluster import KMeans

dim = open(sys.argv[1], "r")
inp = open(sys.argv[2], "r")
out = open(sys.argv[3], "w")

dimension = []
gene = []
matrix = []
dict = {}

def getArray(elements):
    hash = {}
    array = []
    for element in elements:
        hash[element] = 1
    for element in dimension:
        if hash.has_key(element):
            array.append(1)
        else:
            array.append(0)
    return array

def sklearnCluster(numpyArray, num):
    kmeans = KMeans(n_clusters=num).fit(numpyArray)
    cluster = kmeans.predict(numpyArray)
    return cluster

def scipyCluster(numpyArray, num):
    numpyArray = whiten(numpyArray)
    centroid,_ = kmeans(numpyArray, num)
    cluster,_ = vq(numpyArray, centroid)
    return cluster

for line in dim:
    dimension.append(line.rstrip())
for line in inp:
    list = line.split()
    gene.append(list[0])
    elements = list[1].split(",")
    array = getArray(elements)
    matrix.append(array)
numpyArray = numpy.array(matrix)

if(sys.argv[4]=="sklearn"):
    cluster = sklearnCluster(numpyArray, int(sys.argv[5]))
if(sys.argv[4]=="scipy"):
    cluster = scipyCluster(numpyArray, int(sys.argv[5]))

for i in range(len(gene)):
    if dict.has_key(cluster[i]):
        dict[cluster[i]] += "," + gene[i]
    else:
        dict[cluster[i]] = gene[i]
for k,v in dict.items():
    out.write(str(k)+"\t"+str(len(v.split(",")))+"\t"+v+"\n")

dim.close()
inp.close()
out.close()