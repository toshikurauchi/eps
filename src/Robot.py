'''
Created on Sep 30, 2010

@author: Andrew Toshiaki Nakayama Kurauchi
'''
from Dstar import DStar
from State import State

INFINITY = 9999999

def printMatrix(matrix):
    for i in range(len(matrix)):
        print matrix[i]

class Robot:
    def __init__(self, map):
        self.G = State(0,1)
        Init = State(15,0)
        self.dStar = DStar(Init, self.G)
        self.x = Init
        self.map = map
        self.map[Init.row][Init.col] = 2
        self.map[self.G.row][self.G.col] = 3

    def firstSteps(self):
        while self.x.t != "CLOSED":
            if self.dStar.processState() == -1 and self.x.t != "CLOSED":
                return False
        return True
    
    def nextSteps(self):
        while self.dStar.getKMin() < self.x.h:
            if self.dStar.processState() == -1 and self.dStar.getKMin() < self.x.h:
                return False
        return True

    def step(self):
        y = self.x.b
        while not self.isFinished() and self.map[y.row][y.col] != 1:
            self.map[self.x.row][self.x.col] = 0
            self.map[y.row][y.col] = 2
            printMatrix(self.map)
            print " "
            self.x = y
            y = self.x.b
        if self.map[y.row][y.col] == 1:
            self.dStar.modifyCost(self.x, y, INFINITY)
    
    def move(self):
        print "Initial configuration"
        printMatrix(self.map)
        print " "
        print "Starting algorithm..."
        if self.firstSteps():
            self.step()
        while not self.isFinished() and self.nextSteps():
            self.step()

    '''
    def move(self):
        while self.x.t != "CLOSED":
            if self.dStar.processState() == -1 and self.x.t != "CLOSED":
                return False
        y = self.x.b
        if self.map[y.row][y.col] == 1:
            self.dStar.modifyCost(self.x, y, INFINITY)
            while self.dStar.getKMin() < self.x.h:
                if self.dStar.processState() == -1 and self.dStar.getKMin() < self.x.h:
                    return False
        self.map[self.x.row][self.x.col] = 0
        self.map[y.row][y.col] = '*'
        self.x = y
        return True
    '''
    
    def isFinished(self):
        if self.x == self.G:
            return True
        return False