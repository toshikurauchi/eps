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
    numberOfObstacles = int(inputFile.readline())
    obstacles = []
    for i in range(numberOfObstacles):
        obstacles.append((int(inputFile.readline()),int(inputFile.readline())))
    targetReward = float(inputFile.readline())
    forbiddenReward = float(inputFile.readline())
    movementReward = float(inputFile.readline())
    grid = generateGrid(target, forbidden, obstacles, targetReward, forbiddenReward, movementReward)
    print 'Target: ', target
    print 'Forbidden: ', forbidden
    print 'Start: ', start
    print 'Obstacles: ', numberOfObstacles
    print 'Obstacle array: ', obstacles
    print 'Target reward: ', targetReward
    print 'Forbidden reward: ', forbiddenReward
    print 'Movement reward: ', movementReward
    print 'Grid: '
    for line in grid:
        print line
    
def generateGrid(target, forbidden, obstacles, targetReward, forbiddenReward, movementReward):
    "Grid's rows = y, cols = x and the grid is stored reversed"
    grid = [[movementReward]*5, [movementReward]*5, [movementReward]*5, [movementReward]*5, [movementReward]*5]
    grid[target[1]][target[0]] = targetReward
    grid[forbidden[1]][forbidden[0]] = forbiddenReward
    for obstacle in obstacles:
        grid[obstacle[1]][obstacle[0]] = None
    grid.reverse()
    return grid

if __name__ == '__main__':
    sys.exit(main())