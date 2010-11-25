'''
Created on Nov 23, 2010

@author: Andrew Kurauchi
'''
import sys

def main():
    inputFileName = sys.argv[1]
    inputFile = open(inputFileName, 'r')
    "Read target coordinates"
    target = (int(inputFile.readline()),int(inputFile.readline()))
    forbidden = (int(inputFile.readline()),int(inputFile.readline()))
    start = (int(inputFile.readline()),int(inputFile.readline()))
    obstacles = int(inputFile.readline())
    obstacle = []
    for i in range(obstacles):
        obstacle.append((int(inputFile.readline()),int(inputFile.readline())))
    targetReward = float(inputFile.readline())
    forbiddenReward = float(inputFile.readline())
    movementReward = float(inputFile.readline())
    print 'Target: ', target
    print 'Forbidden: ', forbidden
    print 'Start: ', start
    print 'Obstacles: ', obstacles
    print 'Obstacle array: ', obstacle
    print 'Target reward: ', targetReward
    print 'Forbidden reward: ', forbiddenReward
    print 'Movement reward: ', movementReward

if __name__ == '__main__':
    sys.exit(main())