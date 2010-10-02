'''
Created on Sep 30, 2010

@author: Andrew Toshiaki Nakayama Kurauchi
'''
from Dstar import DStar
from definitions import INFINITY, EMPTY, ROBOT

def printMatrix(matrix):
    for i in range(len(matrix)):
        print matrix[i]

class Robot:
    def __init__(self, map, Init, G):
        Init = Init
        self.G = G
        self.dStar = DStar(Init, self.G)
        self.x = Init
        self.map = map

    def firstSteps(self):
        while self.x.t != "CLOSED":
            if self.dStar.processState() == -1 and self.x.t != "CLOSED":
                return False
        return True
    
    def nextSteps(self):
        while self.dStar.getKMin() < self.x.h:
            if self.dStar.processState() == -1 and self.dStar.getKMin() < self.x.h:
                break

    def step(self):
        y = self.x.b
        while not self.isFinished() and self.map[y.row][y.col] != 1:
            self.map[self.x.row][self.x.col] = EMPTY
            self.map[y.row][y.col] = ROBOT
            printMatrix(self.map)
            print " "
            self.x = y
            y = self.x.b
        if not self.isFinished() and self.map[y.row][y.col] == 1:
            self.dStar.modifyCost(y, self.x, INFINITY)
    
    def move(self):
        print "Initial configuration"
        printMatrix(self.map)
        print " "
        print "Starting algorithm..."
        if self.firstSteps():
            self.step()
        while not self.isFinished():
            self.nextSteps() #Assumindo que sempre ha uma solucao, para nao ser necessario tratar buscas infinitas
            self.step()
    
    def isFinished(self):
        if self.x == self.G:
            return True
        return False