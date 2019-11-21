class Graph:
    def __init__(self, name):
        self.name = name
        self.vertices = []
        self.nodeCount = 0
        self.home = False
    def addNode(self, node):
        self.vertices.append(node)
        self.nodeCount += 1
    def printGraph(self):
        print("there are {} nodes in this graph".format(self.nodeCount))
        print("the vertices in the graph are:\n")
        for node in self.vertices:
            if node.neighborCount == 0:
                continue
            print("current node: {} ID:{}".format(node.name, node.ID))
            print("{} neighbors".format(node.neighborCount))
            for neighbor in node.neighbors:
                print("neighbor {}, ID:{}".format(neighbor.name, neighbor.ID))
            print("end node {}\n".format(node.name))


        
                



class Nodex:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.neighbors = []
        self.neighborCount = 0
    def addNegihbor(self, node):
        self.neighbors.append(node)
        self.neighborCount += 1


