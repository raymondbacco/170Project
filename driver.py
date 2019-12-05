
#from optparse import OptionParser
import subprocess
import networkx as nx
import matplotlib.pyplot as plt
import queue
import sys


#usage = "usage: %prog [options] arg"
#parser = OptionParser(usage)
filename = str(sys.argv[1])


#(options, args) = parser.parse_args()
#print(options.filename)
with open('./phase_1_inputs/inputs/'+filename+'.in') as fp:
    numberVertices = fp.readline()   
    #numberVertices = numberVertices[:len(numberVertices)-1]
    numberVertices = numberVertices.replace("\n", "")
    numberHomes = fp.readline()   
    #numberHomes =  numberHomes[:len(numberHomes)-1]  
    numberHomes = numberHomes.replace("\n", "")
    line = fp.readline()   
    nodes = line.split()
    line = fp.readline()
    homes = line.split()
    start = fp.readline()
    start = start.replace("\n", "")
    start = start.replace(" ", "")
#print(homes)

#subprocess.run(["./mst-solver/mstformatter.py", "-f", f'phase_1_inputs/inputs/'+ filename +'.in'])


edges = []
with open("mst_input.txt") as fp:
    line = fp.readline()   
    while line:
        edge = line.split()
        edges.append([edge[1], edge[2],float(edge[3])])
        line = fp.readline()

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)
#plt.subplot(121)
#nx.draw(G)
#plt.show()
totalPath = []
path = dict(nx.all_pairs_shortest_path(G))
q = queue.Queue()

curr = start
print(curr)
#print(homes)
for home in homes:
    q.put(home)
while not q.empty():
    nextHome = q.get()
    if nextHome != start:
        currPath = path[curr][nextHome]
        for node in currPath:
            if node != nextHome:
                totalPath.append(f'{node}')
        curr = nextHome

currPath = path[curr][start]
for node in currPath:
    totalPath.append(f'{node}')

#for i in range(len(homes)):
    #nextNode = homes[i]
#
    #if i < len(homes) - 1:
        #print(f'final node{}'')
        #currPath = path[currNode][nextNode]
        #for node in currPath:
            #if node != nextNode:
                #totalPath.append(f'{node}')
        #currNode = nextNode 
    ##else:
        #currPath = path[currNode][start]
        #for node in currPath:
            #totalPath.append(f'{node}')

print(totalPath)

dropped = []
dropCounts = 0

#f'{filename}.out', 'w')
filePath = f'./outputs/'+ filename +'.out' 
with open(filePath, 'w') as fp:
    fp.write(f'{" ".join(totalPath)}\n')
    for home in totalPath:
        if home in homes and home not in dropped:
            dropped.append(home)
            dropCounts += 1
    assert dropCounts == int(numberHomes), "didn't drop everyone off"
    fp.write(f'{dropCounts}\n')
    dropped = []
    for home in totalPath:
        if home in homes and home not in dropped:
            dropped.append(home)
            fp.write(f'{home} {home}\n') 






#print(totalPath)







