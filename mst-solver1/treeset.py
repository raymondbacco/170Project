'''
Emmanuel John (emmanuj)
TreeSet to represent a set of d-heaps
'''

from node import Node

class TreeSet:
    def __init__(self):
        self.data = {}
    #create set from single node
    def make_set(self, n):
        self.data[n] = Node(n)
    #find set of node n
    def find(self, n):
        gp = self.data[n].parent.parent
        while(gp != self.data[n].parent):
            self.data[n].parent = gp
            n = gp.value
            gp = self.data[n].parent.parent
        return gp.value
    #link 2 nodes
    def union(self, u, v):
        ptr = None
        if self.data[u].rank > self.data[v].rank:
            self.data[v].parent = self.data[u]
            ptr = self.data[u]
        elif self.data[u].rank < self.data[v].rank:
            self.data[u].parent = self.data[v]
            ptr = self.data[v]
        else:
            self.data[u].parent = self.data[v]
            self.data[v].rank = self.data[v].rank + 1
            ptr = self.data[v]
        return ptr
    #for testing purpose
    def printd(self):
        print self.data
