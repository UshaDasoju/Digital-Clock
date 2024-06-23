def create_board():
    return [[' ' for _ in range(7)] for _ in range(6)]
def print_board(board):
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
    print('+---' * 7 + '+')
def is_valid_location(board, col):
    return board[0][col] == ' '
def get_next_open_row(board, col):
    for row in range(5, -1, -1):
        if board[row][col] == ' ':
            return row
def drop_piece(board, row, col, piece):
    board[row][col] = piece
def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(4):
        for r in range(6):
            if all(board[r][c+i] == piece for i in range(4)):
                return True
    # Check vertical locations for win
    for c in range(7):
        for r in range(3):
            if all(board[r+i][c] == piece for i in range(4)):
                return True
    # Check positively sloped diagonals
    for c in range(4):
        for r in range(3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True
    # Check negatively sloped diagonals
    for c in range(4):
        for r in range(3, 6):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True
board = create_board()
game_over = False
turn = 0
print_board(board)
while not game_over:
    col = int(input(f"Player {turn + 1} make your selection (0-6): "))
    if is_valid_location(board, col):
        row = get_next_open_row(board, col)
        drop_piece(board, row, col, 'X' if turn == 0 else 'O')
        if winning_move(board, 'X' if turn == 0 else 'O'):
            print_board(board)
            print(f"Player {turn + 1} wins!")
            game_over = True
        turn = (turn + 1) % 2
        print_board(board)
    else:
        print("Column full! Choose another column.")