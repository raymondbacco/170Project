
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

subprocess.call([ 'python','./mst-solver/mstformatter.py', ('phase_1_inputs/inputs/'+ filename +'.in')])

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
#print(curr)
#print("here")
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

#print(totalPath)
dropoffs=[]
testCount=0
newPath=[]
for node in totalPath:
	newPath.append([node,True])


#Check for repeats of homes one away from a drop point
for n in range(len(totalPath)-2):
	if totalPath[n] == totalPath[n+2]:
		#print([totalPath[n],totalPath[n+1],totalPath[n+2]])
		if(totalPath[n+1] in homes):
			dropoffs.append([totalPath[n],totalPath[n+1]])
			newPath[n+1][1]=False
			newPath[n+2][1]=False
		testCount+=1
optPath=[]
for k in newPath:
	if(k[1]):
		optPath.append(k[0])

#get rid of all the stupid repeats
res = [] 
[res.append(x) for x in dropoffs if x not in res] 
dropoffs=res
#dropoffs is a list of arrays [[first node][home]]

#dropped = []
#dropCounts = 0
#f'{filename}.out', 'w')

filePath = f'./outputs/'+ filename +'.out' 
with open(filePath, 'w') as fp:
    fp.write(f'{" ".join(optPath)}\n')
    # for node in optPath:
    #     if node in homes and node not in dropped:
    #         dropped.append(node)
    #         dropCounts += 1
    #dropCounts += len(dropoffs)

    #setting up output list of drop points
    outputList=[]
    seen=[]
    for node in optPath:

        #check if node is a home and has drop offs
        thisNode = [node]
        if node in homes and node not in seen:
        	seen.append(node)
        	thisNode.append(node)
        	for dps in dropoffs:
        		#print(dps)
        		if dps[0]==node and dps[1] not in optPath:
        			thisNode.append(dps[1])
        	if len(thisNode)>1:
        		outputList.append(thisNode)
    #check for drop of that isn't also a home
    for dps in dropoffs:
        if (dps[0] not in homes and dps[0] not in seen and dps[1] in homes and dps[1] not in seen):
        	seen.append(dps[0])
        	outputList.append(dps)

    # for node in outputList:
    # 	print (node)
    dropCounts= len(outputList)
    #assert dropCounts == int(numberHomes), "didn't drop everyone off"
    fp.write(f'{dropCounts}\n')
    for inserts in outputList:
    	for nodes in inserts:
    		fp.write(nodes+' ')
    	fp.write('\n')

    # for home in totalPath:
    #     if home in homes and home not in dropped:
    #         dropped.append(home)
    #         fp.write(f'{home} {home}\n') 






#print(totalPath)






