grid = [
    ['S',  0,  1,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  1,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  1,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  1,  1,  1,  1,  1,  1,  1,  1 ],
    [  0,  0,  1,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  1,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  1,  0,  0,  0,  0,  0,  0, 'C'],
]

class Node():
    def __init__(self, position, parent):
        self.position = position
        self.parent = parent

        self.g = 0  
        self.h = 0  
        self.f = 0  

    def __eq__(self, other):
        return self.position == other.position

def location(item):
    for row, col in enumerate(grid):
        if item in col:
            j = col.index(item)
            return (row, j)

def cost(cell):
    if grid[cell[0]][cell[1]] == 1:
        return 5
    else:
        return 1

def main():
    start = Node(position=location("S"), parent=None)
    target = Node(position=location("C"), parent=None)

    open_list = []
    closed_list = []

    open_list.append(start)

    while open_list:
        current_node = open_list[0]
        current_index = 0

        for index, node in enumerate(open_list):
            if node.f < current_node.f:
                current_node = node
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node.position == target.position:
            path = []
            total_cost = current_node.f
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return (path[::-1], total_cost)

        neighbors = [(-1, 0), (0, 1), (0, -1), (1, 0)]

        for i, new_cell in enumerate(neighbors):
            node_position = (new_cell[0] + current_node.position[0], new_cell[1] + current_node.position[1])

            if node_position[0] < 0 or node_position[0] >= len(grid) or node_position[1] < 0 or node_position[1] >= len(grid[0]):
                continue

            neighbor = Node(position=node_position, parent=current_node)

            if neighbor in closed_list:
                continue

            if any(open_node for open_node in open_list if neighbor == open_node and neighbor.f >= open_node.f):
                continue
            
            neighbor.g = current_node.g + cost(neighbor.position)
            neighbor.h = abs(neighbor.position[0] - target.position[0]) + abs(neighbor.position[1] - target.position[1])
            neighbor.f = neighbor.g + neighbor.h
            
            open_list.append(neighbor)

if __name__ == "__main__":
    path = main()

    matrix = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    for i , j in enumerate(path[0]):
        matrix[j[0]][j[1]] = 1

    print("The movement map is:\n")
    print(*(j for i , j in enumerate(matrix)) , sep='\n')
    print(f"\nThe path is {path[0]}\nThe cost is {path[1]}")




