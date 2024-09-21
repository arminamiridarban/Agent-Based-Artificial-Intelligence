import math
grid = [
['S', '.', '.', '.', '#', '.', '.', 'G'],
['.', '#', '.', '~', '.', '.', '#', '.'],
['.', '.', '~', '^', '.', '.', '~', '.'],
['.', '#', '.', '.', '.', '#', '.', '.'],
['~', '.', '^', '#', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '~', '.', '.'],
['.', '.', '#', '.', '#', '.', '#', '.'],
['.', '.', '.', '.', '.', '.', '.', '.']
]


class Node():
    def __init__(self, state, parent=None):
        self.state= state
        self.parent = parent

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, node):
        if isinstance(node, Node):
            return (node.state == self.state)
        return False
    
    def __hash__(self):
        return hash(self.state)

def location(grid):
    start, goal, cost_dict = None, None, {}
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if col == 'S':
                start = ((row_index, col_index))
                cost_dict[(row_index, col_index)] = math.inf
            elif col == 'G':
                goal = ((row_index, col_index))
                cost_dict[(row_index, col_index)] = math.inf
            elif col == "#":
                cost_dict[(row_index, col_index)] = math.inf
            elif col == ".":
                cost_dict[(row_index, col_index)] = 1
            elif col == '~':
                cost_dict[(row_index, col_index)] = 3
            elif col == "^":
                cost_dict[(row_index, col_index)] = 5
    return start, goal, cost_dict


def heuristic(current_node, goal):
    startX, startY = current_node.state
    goalX, goalY = goal.state
    return (abs(startX - goalX) + abs(startY - goalY))

start, goal, cost_dict = location(grid)
start, goal = Node(state=start), Node(state=goal)

open_list = []
open_list.append(start)
closed_list = set()

def showPath(path):
    new_grid = [["." for x in range(len(grid))] for y in range(len(grid[0]))]
    for _ in path:
        new_grid[_[0]][_[1]]= "X"
    for _ in new_grid:
        print(_)



while open_list:
    current_node = open_list[0]
    current_node_index = 0
    for index, node in enumerate(open_list):
        if node.f < current_node.f:
            current_node = node
            current_node_index = index

    open_list.pop(current_node_index)
    closed_list.add(current_node)

    if current_node.state == goal.state:
        print("Found the Solution:")
        path = []
        while current_node is not None:
            path.append(current_node.state)
            current_node = current_node.parent
        path = (list(reversed(path)))
        print(path)
        showPath(path)
        break

    possible_actions =[(-1, 0), (0, 1), (0, -1), (1, 0)]

    for move in possible_actions:
        x, y = (current_node.state[0] + move[0]), (current_node.state[1] + move[1])
        if x in range(len(grid)) and y in range(len(grid[0])):
            new_node = Node(state=(x, y), parent=current_node)
            if new_node not in closed_list:
                new_node.g = current_node.g + cost_dict[new_node.state]
                new_node.h = heuristic(new_node, goal)
                new_node.f = new_node.g + new_node.h
                open_list.append(new_node)



