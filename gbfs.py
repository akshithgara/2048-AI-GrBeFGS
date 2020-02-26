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


# Implementation of Iterative Deepening DFS
def gbfs(state, goal, spawnList, gridSize):
    frontier = queue.PriorityQueue()  # Stack implementation

    root = grid(state, '', 0, spawnList, gridSize)
    frontier.put(root)

    explored = []

    while True:
        if frontier.empty():
            break

        curNode = frontier.get()

        if isGoal(curNode.STATE, goal):  # Checks if the goal state is reached.
            return curNode.PATH, curNode

        for child in curNode.CHILDREN(spawnList, gridSize):
            if child.STATE not in explored:
                frontier.put(child)
                explored.append(child.STATE)
