import copy

def matrix_maker(size):
    return [[0] * size for _ in range(size)]


def unitary(board):
    rows = len(board)
    cols = len(board[0])
    # Horizontal Check
    
    for row in board:
        if sum(row) > 1:
            return False
    # Vertical Check
    vertical_sum = [0] * cols

    for col in range(cols):
        for row in range(rows):
            vertical_sum[col] += board[row][col]

    if any(num > 1 for num in vertical_sum):
        return False
    
    # Diagonal Check
    for index, row in enumerate(board):
        for col , _ in enumerate(board):
            x = []
            z = []
            for _ in range(cols):
                if index+_ < len(board) and col+_ < len(board):
                    x.append(board[index+_][col+_])
            for _ in range(cols):
                if col-_ >= 0 and index+_ < len(board):
                    z.append(board[index+_][col-_])
            if sum(x)>1 or sum(z)>1:
                return False
    return True


class Node:
    def __init__(self, board, parent, action):
        self.board = board
        self.action = action
        self.parent = parent


class Frontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)
        
    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        return self.frontier.pop(0)
    
    
def check(board):
    return sum(sum(row) for row in board) == len(board)


def main():
    size = 5
    board = matrix_maker(size)
    node = Node(board, action=None, parent=None)
    frontier = Frontier()
    frontier.add(node)

    solution = []
    while True:
        if check(node.board):
            return node.board
        
        if frontier.empty():
            return "No solution"
        
        node = frontier.remove()
        
        for index, row in enumerate(board):
            for col, _ in enumerate(row):
                if node.board[index][col] == 0:
                    new_board = copy.deepcopy(node.board)
                    new_board[index][col] = 1
                    if unitary(new_board):
                        new_node = Node(board=new_board, parent=node, action=(index, col))
                        frontier.add(new_node)


if __name__ == "__main__":
    solution = main()
    if isinstance(solution, str):
        print("No solution")
    else:
        for row in solution:
            print(row)
