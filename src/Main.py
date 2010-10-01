'''
Created on Oct 1, 2010

@author: Andrew Toshiaki Nakayama Kurauchi
'''
from Robot import Robot

rows = 16
cols = 16

map = [0]*rows
for i in range(rows):
    map[i] = [0]*cols
for i in range(rows):
    map[i][i] = 1
map[15][15] = 0
robot = Robot(map)

robot.move()