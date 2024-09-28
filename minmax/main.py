import math

def print_board(board):
    for r in board:
        print(r)
    print("\n")
board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

def player_turn(board):
    human = 0
    agent = 0
    for r in board:
        for c in r:
            if c == 'X':
                agent += 1
            elif c == 'O':
                human += 1

    if human <= agent:
        return "Human"
    return 'Agent'


def make_move(board, row, col, player):
    if player == 'Agent':
        sign = 'X'
    else:
        sign = 'O'
    if board[row][col] == None:
        board[row][col] = sign

    return board

def get_winner(board):
    for i in range(len(board)):
        if (board[0][i] == board[1][i] == board[2][i]) and board[0][i] != None:
            return board[0][i]
        if (board[i][0] == board[i][1] == board[i][2]) and board[0][i] != None:
            return board[i][0]
    if board[0][0] == board[1][1] == board[2][2] != None:
        return board[1][1]
    if board[2][0] == board[1][1] == board[0][2] != None:
        return board[1][1]
    
    for r in board:
        if any(x == None for x in r):
            return False
    return 'Tie'

def available_moves(board):
    moves = set()
    for r_index, r in enumerate(board):
        for c_index, c in enumerate(r):
            if c == None:
                moves.add((r_index, c_index))
    return moves

def terminal(board):
    winner = get_winner(board)
    if winner:
        return winner
    return None


def minimax(board, is_maximizing_player):
    is_terminal = terminal(board)
    if is_terminal:
        if is_terminal == "X":
            return 1
        elif is_terminal == "O":
            return -1
        elif is_terminal == "Tie":
            return 0
    
    if is_maximizing_player:
        best_score = -math.inf
        for move in available_moves(board):
            row, col = move
            board[row][col] = 'X'
            score = minimax(board, is_maximizing_player=False)
            board[row][col] = None
            best_score = max(score, best_score)
        
        return best_score

    else:
        best_score = math.inf
        for move in available_moves(board):
            row, col = move
            board[row][col] = 'O'
            score = minimax(board, is_maximizing_player=True)
            board[row][col] = None
            best_score = min(score, best_score)
        return best_score
    

def best_move(board):
    best_value = -math.inf
    next_move = None
    for move in available_moves(board):
        r, c = move
        board[r][c] = 'X'
        score = minimax(board, is_maximizing_player=False)
        board[r][c] = None
        if score > best_value:
            next_move = move
            best_value = score
    return next_move

while terminal(board) == None:
    player = player_turn(board)
    if player == "Human":
        print_board(board)
        while True:
            try:
                # Get input and convert to integers
                r = int(input("Select Row in range 0-2: "))
                c = int(input("Select Col in range 0-2: "))
                # Check if the values are in the correct range
                if r not in range(0, 3) or c not in range(0, 3):
                    print("Enter correct values in range 0-2 for rows and columns.")
                    continue  # Re-prompt the user for input
                if (r, c) not in available_moves(board):
                    print("The cell is occupied")
                    continue
                break  # Exit the loop if the inputs are valid
            except ValueError:
                print("Enter integer values in range 0-2 only.")
        board = make_move(board, r, c, player)
    else:
        r, c = best_move(board)
        board = make_move(board, r, c, player)


winner = terminal(board)
print("\n\n**************** GAME OVER ******************\n")
if winner == 'X':
    print("Agent Won!\n")
    print_board(board)
elif winner == "O":
    print("Human Won!\n")
    print_board(board)
else:
    print("It's a Tie!\n")
    print_board(board)
