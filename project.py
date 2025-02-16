import numpy as np
import random
import math

ROWS = 6
COLUMNS = 7
PLAYER_PIECE = 1
AI_PIECE = 2
EMPTY = 0
WINNING_LENGTH = 4

def create_board():
    board = np.zeros((ROWS, COLUMNS), dtype=int)
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    if col >= 0 and col < COLUMNS:
        if board[0][col] == EMPTY:
            return True
    return False

def get_next_open_row(board, col):
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == EMPTY:
            return r

def winning_move(board, piece):
    for r in range(ROWS):
        for c in range(COLUMNS - 3):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    for r in range(ROWS - 3):
        for c in range(COLUMNS):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    for r in range(3, ROWS):
        for c in range(COLUMNS - 3):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

    for r in range(ROWS - 3):
        for c in range(COLUMNS - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    return False

def is_terminal_node(board):
    if winning_move(board, PLAYER_PIECE) or winning_move(board, AI_PIECE):
        return True
    if not any(is_valid_location(board, col) for col in range(COLUMNS)):
        return True
    return False

def score_position(board, piece):
    score = 0
    center_col = [int(i) for i in list(board[:, COLUMNS // 2])]
    score += center_col.count(piece) * 3
    return score

def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = []
    for col in range(COLUMNS):
        if is_valid_location(board, col):
            valid_locations.append(col)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, AI_PIECE):
                return (None, 1000000)
            elif winning_move(board, PLAYER_PIECE):
                return (None, -1000000)
            else:
                return (None, 0)
        else:
            return (None, score_position(board, AI_PIECE))

    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            temp_board = board.copy()
            drop_piece(temp_board, row, col, AI_PIECE)
            new_score = minimax(temp_board, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            if value > alpha:
                alpha = value
            if alpha >= beta:
                break
        return column, value
    else:
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            temp_board = board.copy()
            drop_piece(temp_board, row, col, PLAYER_PIECE)
            new_score = minimax(temp_board, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            if value < beta:
                beta = value
            if alpha >= beta:
                break
        return column, value

def play_game():
    board = create_board()
    game_over = False
    turn = random.randint(0, 1)

    while not game_over:
        if turn == 0:
            try:
                print("Player 1's Turn")
                col = int(input("Pick a column (0-6): "))
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, PLAYER_PIECE)
                    if winning_move(board, PLAYER_PIECE):
                        print("PLAYER 1 WINS!")
                        game_over = True
                else:
                    print("You can not go there. Try again")
            except ValueError:
                print("That's not a number. Enter 0-6")
        else:
            print("AI's Turn")
            col, _ = minimax(board, 5, -math.inf, math.inf, True)
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI_PIECE)
                if winning_move(board, AI_PIECE):
                    print("AI WINS!")
                    game_over = True

        print(np.flip(board, 0))
        turn += 1
        turn %= 2

play_game()