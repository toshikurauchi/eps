'''
Created on Sep 28, 2010

@author: Andrew Toshiaki Nakayama Kurauchi
'''

rows = 16
cols = 16
INFINITY = 9999999

class State:
    def __init__(self, row, col):
        self.t = "NEW"
        self.h = INFINITY
        self.row = row
        self.col = col
        self.initNeighbours()
        self.k = INFINITY
        self.b = None

    def initNeighbours(self):
        self.neighbours = []
        if self.row > 0:
            self.neighbours.append(Neighbour(self.row-1, self.col, 1))
        if self.row < rows - 1:
            self.neighbours.append(Neighbour(self.row+1, self.col, 1))
        if self.col > 0:
            self.neighbours.append(Neighbour(self.row, self.col-1, 1))
        if self.col < cols - 1:
            self.neighbours.append(Neighbour(self.row, self.col+1, 1))

    def c(self, y):
        for i in range(len(self.neighbours)):
            neighbour = self.neighbours[i]
            if neighbour.row == y.row and neighbour.col == y.col:
                return neighbour.cost
        return None
    
    def modifyCost(self, y, cVal):
        for i in range(len(self.neighbours)):
            neighbour = self.neighbours[i]
            if neighbour.row == y.row and neighbour.col == y.col:
                neighbour.cost = cVal
            
class Neighbour:
    def __init__(self, row, col, cost):
        self.row = row
        self.col = col
        self.cost = cost