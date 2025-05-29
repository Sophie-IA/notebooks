def create_board():
    board = [
        ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
        ['bP'] * 8,
        ['  '] * 8,
        ['  '] * 8,
        ['  '] * 8,
        ['  '] * 8,
        ['wP'] * 8,
        ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
    ]
    return board

def print_board(board):
    # print the top column headers
    print("  a  b  c  d  e  f  g  h")
    # loop through each row of the board
    for i, row in enumerate(board):
        # print the row numbers on the left side of the board
        print(8 - i, end = ' ')
        # print each piece in the row with a space in between
        for piece in row:
            print(piece, end = ' ')
        # print the row numbers on the right side of the board
        print(8 - i)
    # print the column headers at the bottom
    print("  a  b  c  d  e  f  g  h")

# run to see initial board
#board = create_board()
#print_board(board)


# BASIC PLAYER INPUT AND MOVEMENT

def parse_position(pos):
    # conver chess notations eg 'e2' to board indices like (6,4)
    columns = 'abcdefgh'
    row = 8 - int(pos[1]) 
    col = columns.index(pos[0])
    return row, col

def move_piece(board, start_pos, end_pos):
    start_row, start_col = parse_position(start_pos)
    end_row, end_col = parse_position(end_pos)

    piece = board[start_row][start_col]

    if piece == '  ':
        print("No piece at starting position!")
        return False
    
    # move the piece
    board[end_row][end_col] = piece
    board[start_row][start_col] = '  '
    return True

# Game loop
def play_chess():
    board = create_board()
    turn = 'w'

    while True:
        print_board(board)
        move = input(f"{'White' if turn == 'w' else 'Black'}'s move (e.g e2 e4): ").lower().strip()

        if move == 'exit':
            break

        try:
            start_pos, end_pos = move.split()
        except ValueError:
            print("Invalid input. Use format like 'e2 e4'.")
            continue

        piece = board[parse_position(start_pos)[0]][parse_position(start_pos)[1]]

        if not piece.startswith(turn):
            print(f"That's not your piece! It's {piece}")
            continue

        success = move_piece(board, start_pos, end_pos)
        if success:
            # switch turns
            turn = 'b' if turn == 'w' else 'w'

#run the game
play_chess()
