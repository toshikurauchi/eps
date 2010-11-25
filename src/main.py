'''
Created on Nov 23, 2010

@author: Andrew Kurauchi
'''
import sys
import mdp

def main():
    input_file_name = sys.argv[1]
    input_file = open(input_file_name, 'r')
    "Read targets coordinates"
    number_of_targets = int(input_file.readline())
    targets = []
    for i in range(number_of_targets):
        targets.append((int(input_file.readline()),int(input_file.readline())))
    "Read forbidden states coordinates"
    number_of_forbiddens = int(input_file.readline())
    forbidden = []
    for i in range(number_of_forbiddens):
        forbidden.append((int(input_file.readline()),int(input_file.readline())))
    terminals = list(targets)
    terminals += forbidden
    "Read initial position"
    start = (int(input_file.readline()),int(input_file.readline()))
    "Read obstacles coordinates"
    number_of_obstacles = int(input_file.readline())
    obstacles = []
    for i in range(number_of_obstacles):
        obstacles.append((int(input_file.readline()),int(input_file.readline())))
    "Read reward value for getting to a target"
    target_reward = float(input_file.readline())
    "Read reward value for getting to a forbidden state"
    forbidden_reward = float(input_file.readline())
    "Read movement cost"
    movement_reward = float(input_file.readline())
    "Read probabilities"
    probabilities = []
    for i in range(4):
        probabilities.append(float(input_file.readline()))
    if(not verify_probabilities(probabilities)):
        sys.exit('The sum of all probabilities must be 1')
    input_file.close()
    grid = generate_grid(targets, forbidden, obstacles, target_reward, forbidden_reward, movement_reward)
    print 'Targets: ', number_of_targets
    print 'Target array: ', targets
    print 'Forbidden states: ', number_of_forbiddens
    print 'Forbidden: ', forbidden
    print 'Terminals: ', terminals
    print 'Start: ', start
    print 'Obstacles: ', number_of_obstacles
    print 'Obstacle array: ', obstacles
    print 'Target reward: ', target_reward
    print 'Forbidden reward: ', forbidden_reward
    print 'Movement reward: ', movement_reward
    print 'Probabilities: ', probabilities
    print 'Grid: '
    for line in grid:
        print line
    grid_mdp = mdp.GridMDP(grid, terminals, start, probabilities)
    U = mdp.value_iteration(grid_mdp, 0.1)
    pi = mdp.best_policy(grid_mdp, U)
    for line in grid_mdp.to_arrows(pi):
        print line
    
def generate_grid(targets, forbidden_states, obstacles, target_reward, forbidden_reward, movement_reward):
    "Grid's rows = y, cols = x and the grid is stored reversed"
    grid = [[movement_reward]*5, [movement_reward]*5, [movement_reward]*5, [movement_reward]*5, [movement_reward]*5]
    for target in targets:
        grid[target[1]][target[0]] = target_reward
    for forbidden in forbidden_states:
        grid[forbidden[1]][forbidden[0]] = forbidden_reward
    for obstacle in obstacles:
        grid[obstacle[1]][obstacle[0]] = None
    grid.reverse()
    return grid

def verify_probabilities(probabilities):
    sum = 0
    for p in probabilities:
        sum += p
    return sum == 1

if __name__ == '__main__':
    sys.exit(main())