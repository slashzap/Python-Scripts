def print_board(board):
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    
def get_move(player, board):
    valid_move = False
    while not valid_move:
        move = input(f"{player}, choose a position (1-9): ")
        if move.isdigit() and int(move) in range(1, 10) and board[int(move) - 1] == ' ':
            return int(move) - 1
        else:
            print("Invalid move. Please try again.")

def check_winner(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return board[i]
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return board[i]
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ' or \
       board[2] == board[4] == board[6] != ' ':
        return board[4]
    # Check if game is a tie
    if ' ' not in board:
        return 'Tie'
    # Game is not over yet
    return None
    
def play_game():
    print("Welcome to Tic Tac Toe!")
    board = [' '] * 9
    players = ['X', 'O']
    turn = 0
    winner = None
    while not winner:
        print_board(board)
        move = get_move(players[turn], board)
        board[move] = players[turn]
        winner = check_winner(board)
        turn = (turn + 1) % 2
    print_board(board)
    if winner == 'Tie':
        print("It's a tie!")
    else:
        print(f"{winner} wins!")
        
        
play_game()
