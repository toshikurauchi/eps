'''
Created on Sep 30, 2010

@author: Andrew Toshiaki Nakayama Kurauchi
'''
from Dstar import DStar
from definitions import INFINITY, EMPTY, ROBOT, OBSTACLE
from copy import deepcopy

class Robot:
    def __init__(self, map, Init, G, log):
        Init = Init
        self.G = G
        self.dStar = DStar(Init, self.G)
        self.x = Init
        self.map = map
        self.path = deepcopy(map)
        self.log = log

    def printMatrix(self, matrix):
        for i in range(len(matrix)):
            self.log.log(matrix[i])

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
        while not self.isFinished() and self.map[y.row][y.col] != OBSTACLE:
            self.map[self.x.row][self.x.col] = EMPTY
            self.map[y.row][y.col] = ROBOT
            self.path[y.row][y.col] = ROBOT
            self.printMatrix(self.map)
            self.log.log(" ")
            self.x = y
            y = self.x.b
        if not self.isFinished() and self.map[y.row][y.col] == OBSTACLE:
            self.dStar.modifyCost(y, self.x, INFINITY)
    
    def move(self):
        self.log.log("Initial configuration")
        self.printMatrix(self.map)
        self.log.log(" ")
        self.log.log("Starting algorithm...")
        if self.firstSteps():
            self.step()
        while not self.isFinished():
            self.nextSteps() #Assumindo que sempre ha uma solucao, para nao ser necessario tratar buscas infinitas
            self.step()
    
    def isFinished(self):
        if self.x == self.G:
            return True
        return False