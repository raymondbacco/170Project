#!/usr/bin/python

from heapq import Heapq
from node import Node
from edge import Edge
from treeset import TreeSet
import sys
import argparse
import fileinput
import time

#read arguments
parser = argparse.ArgumentParser(description='Minimum Spanning Tree (MST) Solver')
parser.add_argument("-d","--heap_d",default=2, type=int, help="balanced head width")
parser.add_argument("-o","--output", help="Output file to write solution")
parser.add_argument("-i","--infile", help="Input graph file. Graph must be in DIMACS format")

args = parser.parse_args()

edges = []
vertices = []
blue_edges =[]

d = int(args.heap_d)
p_queue = Heapq(d)

#read in graph
if(args.infile != None):
    with open(args.infile) as f:
        for line in f:
            #create edges
            if line[0] == "e":
                l = line.split(" ")
                u = int(l[1].strip())
                v = int(l[2].strip())
                w = int(l[3].strip())
                edge = Edge(u, v, w)
                edges.append(edge)
                if u not in vertices:
                    vertices.append(u)
                if v not in vertices:
                    vertices.append(v)
else:
    print "Enter edge line by line in the format e u v w. Press enter each time. Press enter twice when done."
    line = raw_input("==> ")
    while line !="":
        #create edges
        if line[0] == "e":
            l = line.split(" ")
            u = int(l[1].strip())
            v = int(l[2].strip())
            w = int(l[3].strip())
            edge = Edge(u, v, w)
            edges.append(edge)
            if u not in vertices:
                vertices.append(u)
            if v not in vertices:
                vertices.append(v)
        line = raw_input("==> ")

#check for invalid number of nodes and edges
if(len(vertices) <= 0):
    print "Error: Invalid number of nodes"
    exit(0)
if(len(edges) <= 0):
    print "Error: Invalid number of edges"
    exit(0)

#create priority (d-heap) from edges
p_queue.make_heap(edges)

#create nodes with rooted tree set
treeset = TreeSet()
for i in vertices:
    treeset.make_set(i)

#compute min spanning tree starting from smallest edge weight
min_cost = 0
while p_queue.size() != 0:
    edge_i = p_queue.find_min()
    if treeset.find(edge_i.u) != treeset.find(edge_i.v):
        treeset.union(treeset.find(edge_i.u),treeset.find(edge_i.v))
        blue_edges.append(edge_i)
        min_cost = edge_i.weight + min_cost
    p_queue.delete_min()

#write to file
if(args.output == None): #no output file. Write to stdout
    print "c Total cost of tree ", min_cost
    for i in blue_edges:
        print i
else:
    with open(args.output,"w") as f:
        f.write("c Total cost of tree "+ str(min_cost)+"\n")
        for i in blue_edges:
            f.write(str(i)+"\n")
            f.flush()
