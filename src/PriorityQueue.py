'''
Created on Sep 30, 2010

@author: Andrew Toshiaki Nakayama Kurauchi
'''
class PriorityQueue:
    def __init__(self):
        self.Q = []
    
    # Primeiro elemento da fila
    def first(self):
        if len(self.Q) == 0:
            return None
        return self.Q[0]
    
    # Valor associado ao primeiro elemento
    def minVal(self):
        if len(self.Q) == 0:
            return -1
        return self.Q[0].k
    
    # Remove a primeira ocorrencia de x
    def delete(self, x):
        self.Q.remove(x)
        
    # Insere ou reposiciona x na fila
    def placeOrReposition(self, x):
        Q = self.Q
        if x in Q:
            Q.remove(x)
        index = 0
        for i in range(len(Q)):
            if(x.k > Q[i].k):
                index += 1
        Q.insert(index, x)