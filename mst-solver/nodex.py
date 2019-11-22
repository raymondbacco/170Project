import sys

class Graph:
    def __init__(self, name):
        self.name = name
        self.vertices = []
        self.nodeCount = 0
        self.foundHome = False
        self.homeCount = 0
        self.finalHomeNode = 0
        self.finalRouteNode = None
        self.startNode = 0
        self.lastRouteNode = 0
        self.edgeWeights = 16.0
        self.adjMatrix = []
        self.initRoute = []
        self.dijkstraRoute = []
        self.totalRoute = []
        self.droppedAt = {}
        self.newTotalRoute = []

    def addNode(self, node):
        self.vertices.append(node)
        if self.nodeCount == 0:
            self.startNode = node.ID
        self.nodeCount += 1

    def printGraph(self):
        print("there are {} nodes in this graph".format(self.nodeCount))
        print("there are {} homes in this graph".format(self.homeCount))
        print("the start node was:{}".format(self.startNode))
        print("the final home node was:{}".format(self.finalHomeNode))
        print("the final route node was:{}".format(self.finalRouteNode.ID))
        print("the vertices in the graph are:\n")
        for node in self.vertices:
            if node.neighborCount == 0:
                continue
            print("current node: {} ID:{}".format(node.name, node.ID))
            print("{} neighbors".format(node.neighborCount))
            for neighbor in node.neighbors:
                print("neighbor {}, ID:{}".format(neighbor.name, neighbor.ID))
            print("end node {}\n".format(node.name))


    def writeInputFile(self, filename):
        routeNodes = []
        homeNames = []
        vertexNames = []
        adjMatrix = []
        s = " "
        for node in self.vertices:
            if node.routeNode:
                routeNodes.append(node.name)
            if node.homeNode:
                homeNames.append(node.name)
            vertexNames.append(node.name)
        print(routeNodes)
        self.initRoute = routeNodes
            
        with open(f'{filename}.in', 'w') as the_file:
            the_file.write(f'{self.nodeCount}\n')
            the_file.write(f'{self.homeCount}\n')
            the_file.write(f'{" ".join(vertexNames)}\n')
            the_file.write(f'{" ".join(homeNames)}\n')
            the_file.write(f'{self.vertices[self.startNode].name}\n')
            for i in range(self.nodeCount):
                adjMatrix.append(['x'] * self.nodeCount)
            for node in self.vertices:
                for neighbor in node.neighbors:
                    adjMatrix[node.ID][neighbor.ID] = str(self.edgeWeights)
            for i in range(len(adjMatrix)):
                for j in range(len(adjMatrix)):
                    adjMatrix[j][i] = adjMatrix[i][j]
            for i in range(self.nodeCount):
                the_file.write(f'{" ".join(adjMatrix[i])}\n')
            self.adjMatrix = adjMatrix

        print(self.finalRouteNode.ID)
    def writeOutputFile(self, filename):
        with open(f'{filename}.out', 'w') as the_file:
            the_file.write(f'{" ".join(self.totalRoute)}\n')
            the_file.write(f'{len(self.droppedAt)}\n')
            for location, droppedAtNames in self.droppedAt.items():
                the_file.write(f'{location} {" ".join(droppedAtNames)}\n')

        return

    def setHomeNode(self, node, numHomes):
        if self.homeCount < numHomes:
            node.homeNode = True
            self.homeCount+=1
            if self.homeCount == numHomes:
                self.foundHome = True
                self.finalHomeNode = node.ID
                self.finalRouteNode = self.lastRouteNode
    '''
    def setRouteNode(self, node):
        if self.foundHome != True:
            node.routeNode = True
            self.lastRouteNode = node
    '''
    def addRouteNode(self, node):
        if self.foundHome != True:
            node.routeNode = True
            self.lastRouteNode = node
            self.newTotalRoute.append(node.name)
    

    def dijkstra(self, start, end):

        def minDistance( dist, sptSet): 
        # Initilaize minimum distance for next node 
            min = sys.maxsize
            # Search not nearest vertex not in the  
            # shortest path tree 
            #print(self.nodeCount)
            for v in range(self.nodeCount):
                #print(str(dist[v] < min)+" "+str(sptSet[v] == False)) 
                if dist[v] < min and sptSet[v] == False: 
                    min = dist[v] 
                    min_index = v 
            return min_index

        #dijkstra starts
        dist = [sys.maxsize] * self.nodeCount 
        dist[start] = 0
        sptSet = [False] * self.nodeCount 
        prev = [0 for column in range(self.nodeCount)]

        matrix=[]
        for u in self.adjMatrix:
            row = []
            for elem in u:
                if elem == "x" or elem == "x\n":
                    row.append(0)
                elif elem == ""or elem =='' or elem =='\n':
                    None
                else:
                    #print(elem)
                    row.append(float(elem))
            matrix.append(row)
                #rint(row)
        #rint (matrix)
        for cout in range(self.nodeCount): 
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration

            u = minDistance(dist, sptSet) 
            # Put the minimum distance vertex in the  
            # shotest path tree 
            sptSet[u] = True

            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.nodeCount):
                #print(self.adjMatrix)
                if (matrix[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + matrix[u][v]): 
                        dist[v] = dist[u] + matrix[u][v]
                        prev[v] = u 
        

        #print path
        #print(start)
        #print(end)
        #print(prev)
        p = [end]
        #print(prev[end])
        while end != start:
            #print(prev[end])
            p.append(prev[end])
            end = prev[end]
        #print(p)
        q = list(reversed(p))
        #print(q)
        ind=0
        for w in q:
            q[ind] = self.vertices[w].name
            ind+=1
        self.dijkstraRoute = q
        #print(path_string)


class Nodex:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.neighbors = []
        self.neighborCount = 0
        self.routeNode = False
        self.dropNode = False
        self.homeNode = False
    def addNeighbor(self, node):
        self.neighbors.append(node)
        self.neighborCount += 1


