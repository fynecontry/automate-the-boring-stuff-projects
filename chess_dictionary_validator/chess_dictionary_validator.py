#!/usr/bin/env python3

def is_valid_chess_board(board):
    '''Check is a given chess board is valid'''
    
    MAX_PIECES = 16     # Maximum no of pieces size
    MAX_PAWNS = 8       # Maximum no of pawns
    VALID_ROWS = ['1','2','3','4','5','6','7','8']
    VALID_COLS = ['a','b','c','d','e','f','g','h']
    VALID_PLAYERS = ('b', 'w')
    SUITS = ('pawn', 'knight', 'bishop', 'rook', 'queen', 'king')


    # Check board contains only 1 bking and 1 wking
    if not (list(board.values()).count('bking') == list(board.values()).count('wking') == 1):
        return False

    # Count no of pieces each player has
    no_black_pieces = 0
    no_white_pieces = 0
    for val in board.values():
        if val.startswith('b'):
            no_black_pieces += 1
        elif val.startswith('w'):
            no_white_pieces += 1
        else:
            return False    # Not valid if value doesnt start with 'b' or 'w'
    
    # Check if no piece exceed max pieces(16) allowed for each player  
    if no_black_pieces > MAX_PIECES or no_white_pieces > MAX_PIECES:
        return False
    
    # Count no of pawns each player has & check if exceeds max no of pawns (8) allowed
    no_b_pawns = list(board.values()).count('bpawn')
    no_w_pawns = list(board.values()).count('wpawn')
    if no_b_pawns > MAX_PAWNS or no_w_pawns > MAX_PAWNS:
        return False

    # Extract key individual strings to check for valid space
    board_key_rows = [ key[:1] for key in board.keys()]
    board_key_cols = [ key[1:] for key in board.keys()]
    # Check if key rows & cols are valid spaces 1-8 a-h
    if not (all(key_row in VALID_ROWS for key_row in board_key_rows) and 
            all(key_col in VALID_COLS for key_col in board_key_cols)):
        return False

    # Check values start with 'b' or 'w' and ends with valid suits
    for val in board.values():
        if not (val.startswith((VALID_PLAYERS)) and val.endswith((SUITS))):
            return False



    return True


def main():
    ''' Main program'''
    # Sample sets for test
    print(is_valid_chess_board({'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '3d': 'bpawn', '2b': 'wpawn', '5f': 'bpawn'}))           # True a valid board!

 
    print(is_valid_chess_board({"1a": "bpawn", "2a": "wking"}))         # False: no bking
    print(is_valid_chess_board({"1a": "wking", "2a": "wking", "3c": "bbishop"}))    # False cannot have 2 white kings
    print(is_valid_chess_board({"1a": "bking", "9z": "wking"}))         # False: 9z is an invalid position

if __name__ == "__main__":
    main()
