class Graph:
    def __init__(self, name):
        self.name = name
        self.vertices = []
        self.nodeCount = 0.0
        self.home = False
        self.homeCount = 0.0
        self.finalHomeNode = 0.0
        self.startNode = 0.0
    def addNode(self, node):
        self.vertices.append(node)
        if self.nodeCount == 0:
            self.startNode = node.ID
        self.nodeCount += 1
    def printGraph(self):
        print("there are {} nodes in this graph".format(self.nodeCount))
        print("there are {} homes in this graph".format(self.homeCount))
        print("the start node was:{}".format(self.startNode))
        print("the final node was:{}".format(self.finalHomeNode))
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
        for node in self.vertices:
            if node.routeNode:
                routeNodes.append([node.ID, node.name])
        print(routeNodes)

class Nodex:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.neighbors = []
        self.neighborCount = 0
        self.routeNode = False
        self.dropNode = False
        self.homeNode = False
    def addNegihbor(self, node):
        self.neighbors.append(node)
        self.neighborCount += 1


