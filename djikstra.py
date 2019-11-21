import sys
import numpy as np
import random
import ast

filename = sys.argv[1]
f = open(filename, 'r')
lines=f.readlines()
num_nodes = int(lines[0])
#print(num_nodes)
num_homes = int(lines[1])
#print(num_homes)
names = lines[2].split(" ")
home_names = lines[3].split(" ")
start_name = lines[4]
#count=0
matrix=[]
for u in range(num_nodes):
    readline = lines[5+u]
    readline = readline.split(" ")
    row = []
    for elem in readline:
        if elem == "x":
            row.append(0)
        elif elem == ""or elem =='' or elem =='\n':
            None
        else:
            #print(elem)
            row.append(float(elem))
    matrix.append(row)
    #count+=1
    #print(count)
npMatrix=np.array(matrix)

class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                      for row in range(vertices)]
        self.prev = [0 for column in range(vertices)] 
  
    def printSolution(self, dist): 
        print("Vertex tDistance from Source")
        for node in range(self.V): 
            print (node, "dist From start:", dist[node] )
  
    # A utility function to find the vertex with  
    # minimum distance value, from the set of vertices  
    # not yet included in shortest path tree 
    def minDistance(self, dist, sptSet): 
  
        # Initilaize minimum distance for next node 
        min = sys.maxsize
  
        # Search not nearest vertex not in the  
        # shortest path tree 
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
  
        return min_index 
  
    # Funtion that implements Dijkstra's single source  
    # shortest path algorithm for a graph represented  
    # using adjacency matrix representation 
    def dijkstra(self, src): 
  
        dist = [sys.maxsize] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
  
        for cout in range(self.V): 
  
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.minDistance(dist, sptSet) 
  
            # Put the minimum distance vertex in the  
            # shotest path tree 
            sptSet[u] = True
  
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
                if (self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]): 
                        dist[v] = dist[u] + self.graph[u][v]
                        self.prev[v] = u 
  
        #self.printSolution(dist) 
        #print(self.prev)

g = Graph(num_nodes)
g.graph =matrix
g.dijkstra(0)
#print(g.prev)

try:
    start = int(sys.argv[2])
    end = int(sys.argv[3])
    path = True
except:
    path=False

if path:
    p = [end]
    while end != start:
        p.append(g.prev[end])
        end = g.prev[end]
    q = list(reversed(p))
    path_string=""
    for w in q:
        path_string +=(names[w]+ " ")
    print(path_string)
