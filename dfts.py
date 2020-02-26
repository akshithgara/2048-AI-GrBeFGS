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
def ID_DFTS(state, goal, spawnList, gridSize):
    frontier = queue.LifoQueue() # Stack implementation

    root = grid(state, '', 0, spawnList, gridSize)
    bound = 0  # Initializing max depth to zero.
    natural_failure = False # Setting it to false, so that we toggle only we run out of any more nodes to explore.
    while not natural_failure:
        frontier.put(root)
        while True:
            if frontier.empty():
                break

            curNode = frontier.get()

            if isGoal(curNode.STATE, goal):     # Checks if the goal state is reached.
                return curNode.PATH, curNode
            children = curNode.CHILDREN(spawnList, bound, gridSize)
            if len(curNode.PATH) < bound:  # As long as it is within the depth limit.
                if not children: # Sets natural failure to True only when we run out of states to explore.
                    natural_failure = True
                else:
                    for child in children:
                        natural_failure = False # Sets it to false to keep the loop running as along as there are
                        # more children nodes to explore.
                        frontier.put(child)
        bound += 1
