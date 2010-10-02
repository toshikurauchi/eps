'''
Created on Sep 28, 2010

@author: Andrew Toshiaki Nakayama Kurauchi
'''
from definitions import INFINITY, rows, cols

class State:
    def __init__(self, row, col):
        # Os nomes dos atributos foram escolhidos de acordo com os utilizados no artigo de Anthony Stentz
        # Dado um State x, temos:
        self.t = "NEW" # t(x)
        self.h = INFINITY # h(x)
        self.row = row # linha de x na matriz (tanto na matriz de estados quanto no mapa)
        self.col = col # coluna de x na matriz (tanto na matriz de estados quanto no mapa)
        self.initNeighbours() # cria uma lista de Neighbour's, que guarda o custo c(x, Neighbour)
        self.k = INFINITY # k(x)
        self.b = None # b(x)

    # Se o State nao estao nas bordas ele tem todos os 4 vizinhos
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
    
    # Calcula o custo c(self, y) conforme definido no artigo
    def c(self, y):
        for i in range(len(self.neighbours)):
            neighbour = self.neighbours[i]
            if neighbour.row == y.row and neighbour.col == y.col:
                return neighbour.cost
        return None
    
    # Modifica o custo c(x, y) para cVal
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