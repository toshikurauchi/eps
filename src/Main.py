'''
Created on Oct 1, 2010

@author: Andrew Toshiaki Nakayama Kurauchi
'''
from Robot import Robot
from definitions import rows, cols
from State import State

map = [0]*rows
for i in range(rows):
    map[i] = [0]*cols
for i in range(rows):
    map[i][i] = 1
map[15][15] = 0
robot = Robot(map, State(15,0), State(0,15))

robot.move()