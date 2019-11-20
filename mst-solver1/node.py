'''
Emmanuel John (emmanuj)

Encapsulates node data
'''
class Node:
    def __init__(self, val):
        self.value = val
        self.parent = self
        self.rank = 0
    def __repr__(self):
        return "n "+str(self.value)+" r "+ str(self.rank) + " p "+ str(self.parent.value)
