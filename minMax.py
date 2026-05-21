board = [" " for _ in range(9)]

winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  
    [0, 4, 8], [2, 4, 6]  
]

def is_board_full():
    return " " not in board

def is_winner(player):
    for combination in winning_combinations:
        if all( board[i] == player for i in combination):
            return True
    return False
def get_possible_move():
    return [i for i, x in enumerate(board) if x == " "]

def min_max(position, depth, maximizing_player):
    if is_winner("O"):
        return 1
    elif is_winner("X"):
        return -1
    elif is_board_full():
        return 0
    
    if maximizing_player:
        max_eval = float("inf")
        for move in get_possible_move():
            board[move] = "O"
            eval = min_max( position + 1, depth - 1, False)
            board[move] = " "
            max_eval = max(eval, max_eval)
        
        return max_eval
    else:
        min_eval = - float("inf")
        for move in get_possible_move():

            board[move] = "X"
            eval = min_max( position + 1, depth - 1, True)
            min_eval = min( min_eval, eval)
            board[move] = " "
        return min_eval

def ai_move():
    best_score = - float("inf")
    best_move = None

    for move in get_possible_move():
        board[move] = "O"
        eval = min_max(0, len(get_possible_move()), False)
        board[move] = " "
        if eval >= best_score:
            best_score = eval
            best_move = move
    board[best_move] = "O"

def player_move():
    valid_moves = get_possible_move()
    move = -1
    while move not in valid_moves:
        move = int(input("Enter a valid number(0 - 8)"))

    board[move] = "X"

def print_board():
    print('-------------')
    for i in range(0, 9, 3):
        print('|', board[i], '|', board[i+1], '|', board[i+2], '|')
        print('-------------')

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while not is_board_full():
        player_move()
        # print_board()

        if is_winner('X'):
            print("Congratulations! You won!")
            return
        ai_move()
        print_board()

        if is_winner('O'):
            print("You lost!")
            return

        if is_board_full():
            print("It's a draw!")
            return

    print("It's a draw!")

play_game()