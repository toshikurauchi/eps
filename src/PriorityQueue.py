'''
Created on Sep 30, 2010

@author: Andrew Toshiaki Nakayama Kurauchi
'''
class PriorityQueue:
    def __init__(self):
        self.Q = []
    
    def first(self):
        if len(self.Q) == 0:
            return None
        return self.Q[0]
    
    def minVal(self):
        if len(self.Q) == 0:
            return -1
        return self.Q[0].k
    
    def delete(self, x):
        self.Q.remove(x)
        
    def placeOrReposition(self, x):
        Q = self.Q
        if x in Q:
            Q.remove(x)
        index = 0
        for i in range(len(Q)):
            if(x.k > Q[i].k):
                index += 1
        Q.insert(index, x)