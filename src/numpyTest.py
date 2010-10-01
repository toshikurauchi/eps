'''
Created on Sep 28, 2010

@author: Andrew Toshiaki Nakayama Kurauchi
'''

import numpy as np

class Teste:
    def __init__(self, a, b):
        self.a = a
        self.b = b

m = np.matrix([[Teste(1,2),Teste(2,3)],[Teste(3,4),Teste(4,5)]])
for i in range(2):
    for j in range(2):
        print m[i,j].a
        
mat = [0]*4
for i in range(4):
    mat[i] = [0]*3
    
for i in range(4):
    for j in range(3):
        mat[i][j] = i+j
        
print mat

a = Teste(1, 2)
b = a
b.a = 3
print a.a

print min(1, 2)

lista = [a]
a.a = 10
print lista.count(a)
print lista.count(b)
print lista.count(Teste(4,5))

ns = [1,2,3]
print ns
ns.insert(1, 99)
print ns
ns.insert(4, 100)
print ns

index = 0
index += 1
print index

a = Teste(1,2)
lista = [a, Teste(2,3), Teste(3,4)]
for i in lista:
    print i.a
    
print range(len(lista))

print len(mat)

print a in lista