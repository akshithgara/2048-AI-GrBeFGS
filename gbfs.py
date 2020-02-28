import queue
from grid import grid


# Function to check if the goal state has been achieved.
def isGoal(state, goal):
    win = goal
    for line in state:
        for i in line:
            if i == win:
                return True
    return False


# Implementation of Greedy Best First Search
def gbfs(state, goal, spawnList, gridSize):
    frontier = queue.PriorityQueue()  # Priority Queue Implementation

    root = grid(state, '', 0, spawnList, gridSize)
    frontier.put(root)

    explored = []

    while not frontier.empty():

        curNode = frontier.get()

        if isGoal(curNode.STATE, goal):
            # print(curNode.STATE)# Checks if the goal state is reached.
            return curNode.PATH, curNode

        else:
            for child in curNode.CHILDREN(spawnList, gridSize):
                visited = False
                for i in explored:
                    # print(i)
                    if i == child.STATE:
                        visited = True
                if not visited:
                    frontier.put(child)
                    explored.append(child.STATE)
