'''
Created on Oct 1, 2010

@author: Andrew Toshiaki Nakayama Kurauchi
'''
from Robot import Robot
from definitions import rows, cols, ROBOT, GOAL, EMPTY, OBSTACLE
from State import State
import sys
from Logger import LOGGER
from random import randint

# Cria mapa vazio
map = [0]*rows
for i in range(rows):
    map[i] = [EMPTY]*cols
    
# Abre arquivo de entrada
filename = ""
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    print "Input file name not specified"
    sys.exit(0)
input = open(filename, "r")

# Leitura das barreiras
line = input.readline()
nLines = int(line.split()[0])
while nLines:
    line = input.readline()
    coordinates = line.split()
    row = int(coordinates[0])
    col = int(coordinates[1])
    map[row][col] = OBSTACLE
    nLines -= 1

# Leitura do estado inicial
line = input.readline()
coordinates = line.split()
row = int(coordinates[0])
col = int(coordinates[1])
if row == -1 and col == -1:
    generated = False
    while not generated:
        row = randint(0,15)
        col = randint(0,15)
        if map[row][col] == EMPTY:
            generated = True
Init = State(row, col)
map[Init.row][Init.col] = ROBOT
# Leitura do estado final
line = input.readline()
coordinates = line.split()
row = int(coordinates[0])
col = int(coordinates[1])
if row == -1 and col == -1:
    generated = False
    while not generated:
        row = randint(0,15)
        col = randint(0,15)
        if map[row][col] == EMPTY:
            generated = True
G = State(row, col)
map[G.row][G.col] = GOAL

input.close()
log = LOGGER()
log.startLog()
    
# Executa o algoritmo
robot = Robot(map, Init, G, log)
robot.move()

log.endLog()

# Imprime caminho no arquivo de saida
if len(sys.argv) > 2:
    output = open(sys.argv[2], "w")
    for line in robot.path:
        output.write(str(line)+"\n")
    output.close()
