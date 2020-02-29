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

    explored = set()

    while not frontier.empty():

        curNode = frontier.get()
        # print(curNode.STATE)
        if isGoal(curNode.STATE, goal):
            # print(curNode.STATE)# Checks if the goal state is reached.
            return curNode.PATH, curNode

        else:
            for child in curNode.CHILDREN(spawnList, gridSize):
                visited = child in explored
                if not visited:
                    frontier.put(child)
                    explored.add(child)

