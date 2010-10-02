'''
Created on Sep 30, 2010

@author: Andrew Toshiaki Nakayama Kurauchi
'''
from Dstar import DStar
from definitions import INFINITY, EMPTY, ROBOT, OBSTACLE
from copy import deepcopy

class Robot:
    def __init__(self, map, Init, G, log):
        # Os nomes dos atributos foram escolhidos conforme descrito no artigo de Anthony Stentz
        Init = Init # Posicao inicial
        self.G = G # Alvo
        self.dStar = DStar(Init, self.G) # Implementacao do algoritmo
        self.x = Init # x guarda a posicao atual do robo
        self.map = map # mapa real (desconhecido para o robo)
        self.path = deepcopy(map) # copia do mapa, para guardar o caminho percorrido
        self.log = log # classe utilizada para guardar cada movimento do robo

    def printMatrix(self, matrix):
        for i in range(len(matrix)):
            self.log.log(matrix[i])

    # Passos realizados ate que o estado inicial saia da OPEN list
    def firstSteps(self):
        while self.x.t != "CLOSED":
            if self.dStar.processState() == -1 and self.x.t != "CLOSED":
                return False
        return True
    
    # Passos realizados apos encontrar alguma barreira
    def nextSteps(self):
        while self.dStar.getKMin() < self.x.h:
            if self.dStar.processState() == -1 and self.dStar.getKMin() < self.x.h:
                break

    # Segue o caminho escolhido ate que seja encontrado o alvo (fim do algoritmo), ou alguma barreira
    def step(self):
        y = self.x.b
        while not self.isFinished() and self.map[y.row][y.col] != OBSTACLE:
            self.map[self.x.row][self.x.col] = EMPTY
            self.map[y.row][y.col] = ROBOT
            self.path[y.row][y.col] = ROBOT # Para o arquivo de saida
            self.printMatrix(self.map)
            self.log.log(" ")
            self.x = y
            y = self.x.b
        if not self.isFinished() and self.map[y.row][y.col] == OBSTACLE:
            self.dStar.modifyCost(y, self.x, INFINITY)
    
    # Anda ate encontrar o alvo
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