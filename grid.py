# Akshith Gara
# 2048 AI
# CS5400


def transpose(field):
    return [list(row) for row in zip(*field)]


def invert(field):
    return [row[::-1] for row in field]


# Function to check if a move in a particular direction is possible.
def move_is_possible(direction, field1):
    def row_is_left_movable(row):
        def change(i):  # true if there'll be change in i-th tile
            if row[i] == 0 and row[i + 1] != 0:  # Move
                return True
            if row[i] != 0 and row[i + 1] == row[i]:  # Merge
                return True
            return False

        return any(change(i) for i in range(len(row) - 1))

    # //direction   0: up, 1: right, 2: down, 3: left
    check = {}
    check['Left'] = lambda field: \
        any(row_is_left_movable(row) for row in field)

    check['Right'] = lambda field: \
        check['Left'](invert(field))

    check['Up'] = lambda field: \
        check['Left'](transpose(field))

    check['Down'] = lambda field: \
        check['Right'](transpose(field))

    if direction in check:
        # //direction   0: up, 1: right, 2: down, 3: left
        return check[direction](field1)
    else:
        return False


# Function to spawn values as per the given guidelines
def spawn(field, spawnNums, spawnCount, size):
    new_element = spawnNums[spawnCount]
    if field[0][0] == 0:
        field[0][0] = new_element
    elif field[0][size[0] - 1] == 0:
        field[0][size[0] - 1] = new_element
    elif field[size[1] - 1][size[0] - 1] == 0:
        field[size[1] - 1][size[0] - 1] = new_element
    elif field[size[1] - 1][0] == 0:
        field[size[1] - 1][0] = new_element
    else:
        return


# Grid class to perform moves and add up values if they match
class grid:

    def __init__(self, state, path, spawn, spawn_list, size):
        self.STATE = state
        self.PATH = path
        self.SPAWN = spawn
        self.spawnList = spawn_list
        self.size = size

    def move(self, direction, spawnVal):
        def move_row_left(row):
            def tighten(row):  # squeeze non-zero elements together
                new_row = [i for i in row if i != 0]
                new_row += [0 for i in range(len(row) - len(new_row))]
                return new_row

            def merge(row):
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:
                        new_row.append(2 * row[i])
                        # self.score += 2 * row[i]
                        pair = False
                    else:
                        if i + 1 < len(row) and row[i] == row[i + 1]:
                            pair = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row) == len(row)
                return new_row

            return tighten(merge(tighten(row)))

        moves = {}
        moves['Left'] = lambda field: \
            [move_row_left(row) for row in field]
        moves['Right'] = lambda field: \
            invert(moves['Left'](invert(field)))
        moves['Up'] = lambda field: \
            transpose(moves['Left'](transpose(field)))
        moves['Down'] = lambda field: \
            transpose(moves['Right'](transpose(field)))

        if direction in moves:
            # Spawns the values circularly
            if move_is_possible(direction, self.STATE):
                self.STATE = moves[direction](self.STATE)
                if spawnVal > len(self.spawnList) - 1:
                    spawnVal = spawnVal % len(self.spawnList)
                spawn(self.STATE, self.spawnList, spawnVal, self.size)
                return True
            else:
                return False

    def CHILDREN(self, sl, depth, gridSize):  # Function to try out all the moves and add it to the childList.
        if len(self.PATH) >= depth: # Doesn't explore anymore children nodes and returns out if the depth limit is hit.
            return []

        childList = []
        for direction in ['Up', 'Down', 'Left', 'Right']:
            curGrid = grid(state=self.STATE, path=self.PATH, spawn=self.SPAWN, spawn_list=sl, size=gridSize)
            if curGrid.move(direction, self.SPAWN):
                # Generate the state for the child
                childState = curGrid.STATE
                child = grid(childState, ''.join([self.PATH, direction[0]]), self.SPAWN + 1, spawn_list=sl,
                             size=gridSize)
                childList.append(child)

        return childList
