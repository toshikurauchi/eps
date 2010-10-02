'''
Created on Sep 28, 2010

@author: Andrew Toshiaki Nakayama Kurauchi
'''
from State import State
from PriorityQueue import PriorityQueue
from definitions import INFINITY

class DStar:
    def init_matrix(self):
        self.states = [0]*self.rows
        for i in range(self.rows):
            self.states[i] = [0]*self.cols
            
        for i in range(self.rows):
            for j in range(self.cols):
                self.states[i][j] = State(i,j)
    
    def __init__(self, Init, G):
        self.open = PriorityQueue()
        self.rows = 16
        self.cols = 16
        self.init_matrix()
        self.states[Init.row][Init.col] = Init
        self.states[G.row][G.col] = G
        self.insert(G, 0)
    
    def minState(self):
        return self.open.first()
    
    def getKMin(self):
        return self.open.minVal()
    
    def delete(self, x):
        x.t = "CLOSED"
        x.k = INFINITY
        self.open.delete(x)
    
    def insert(self, x, hNew):
        if x.t == "NEW":
            x.k = hNew
        if x.t == "OPEN":
            x.k = min(x.k, hNew)
        if x.t == "CLOSED":
            x.k = min(x.h, hNew)
        x.h = hNew
        x.t = "OPEN"
        self.open.placeOrReposition(x)
    
    def neighborsOf(self, x):
        neighbours = []
        for neighbour in x.neighbours:
            neighbours.append(self.states[neighbour.row][neighbour.col])
        return neighbours
    
    def processState(self):
        x = self.minState()
        if x is None:
            return -1
        kOld = self.getKMin()
        self.delete(x)
        if kOld < x.h:
            for y in self.neighborsOf(x):
                if y.h <= kOld and x.h > y.h + y.c(x):
                    x.b = y
                    x.h = y.h + y.c(x)
        if kOld == x.h:
            for y in self.neighborsOf(x):
                if y.t == "NEW" or (y.b == x and y.h != x.h + x.c(y)) or (y.b != x and y.h > x.h + x.c(y)):
                    y.b = x
                    self.insert(y, x.h + x.c(y))
        else:
            for y in self.neighborsOf(x):
                if y.t == "NEW" or (y.b == x and y.h != x.h + x.c(y)):
                    y.b = x
                    self.insert(y, x.h + x.c(y))
                else:
                    if y.b != x and y.h > x.h + x.c(y):
                        self.insert(x, x.h)
                    else:
                        if y.b != x and x.h > y.h + y.c(x) and y.t == "CLOSED" and y.h > kOld:
                            self.insert(y, y.h)
        return self.getKMin()
        
    def modifyCost(self, x, y, cVal):
        x.modifyCost(y, cVal)
        if x.t == "CLOSED":
            self.insert(x, x.h)
        return self.getKMin()
