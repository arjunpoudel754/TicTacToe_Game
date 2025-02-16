
board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

game_ongoing = True
winner = None
current_player = "X"

def print_board():
    print("\n".join([" | ".join(board[:3])," | ".join(board[3:6])," | ".join(board[6:9])]))

def play_game():
    print_board()

    while game_ongoing:
        handle_turn(current_player)

        check_game_over()
        if not game_ongoing:
            break
        flip_player()
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "_":
            valid = True
        else:
            print("You can't go there. Go again.")

    board[position] = player
    print_board()

def check_game_over():
    check_winner()
    check_tie()

def check_winner():
    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

def check_rows():
    global game_ongoing
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"

    if row_1 or row_2 or row_3:
        game_ongoing = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

def check_columns():
    global game_ongoing
    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[2] == board[5] == board[8] != "_"

    if column_1 or column_2 or column_3:
        game_ongoing = False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

def check_diagonals():
    global game_ongoing
    diagonal_1 = board[0] == board[4] == board[8] != "_"
    diagonal_2 = board[2] == board[4] == board[6] != "_"

    if diagonal_1 or diagonal_2:
        game_ongoing = False

    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]

def check_tie():
    global game_ongoing
    if "_" not in board:
        game_ongoing = False
        return True
    else:
        return False

def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

play_game()