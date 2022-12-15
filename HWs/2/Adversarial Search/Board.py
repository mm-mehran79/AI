import numpy as np

ROWS = 7
COLS = 9


class BoardUtility:
    @staticmethod
    def make_move(game_board, col, piece):
        """
        make a new move on the board
        row & col: row and column of the new move
        piece: 1 for first player. 2 for second player
        """
        row = BoardUtility.get_next_open_row(game_board, col)
        assert game_board[row][col] == 0
        game_board[row][col] = piece

    @staticmethod
    def is_column_full(game_board, col):
        return game_board[0][col] != 0

    @staticmethod
    def get_next_open_row(game_board, col):
        """
        returns the first empty row in a column from the top.
        useful for knowing where the piece will fall if this
        column is played.
        """
        for r in range(ROWS - 1, -1, -1):
            if game_board[r][col] == 0:
                return r

    @staticmethod
    def has_player_won(game_board, player_piece):
        """
        piece:  1 or 2.
        return: True if the player with the input piece has won.
                False if the player with the input piece has not won.
        """
        # checking horizontally
        for c in range(COLS - 3):
            for r in range(ROWS):
                if game_board[r][c] == player_piece and game_board[r][c + 1] == player_piece and game_board[r][
                    c + 2] == player_piece and game_board[r][c + 3] == player_piece:
                    return True

        # checking vertically
        for c in range(COLS):
            for r in range(ROWS - 3):
                if game_board[r][c] == player_piece and game_board[r + 1][c] == player_piece and game_board[r + 2][
                    c] == player_piece and game_board[r + 3][c] == player_piece:
                    return True

        # checking diagonally
        for c in range(COLS - 3):
            for r in range(3, ROWS):
                if game_board[r][c] == player_piece and game_board[r - 1][c + 1] == player_piece and game_board[r - 2][
                    c + 2] == player_piece and \
                        game_board[r - 3][c + 3] == player_piece:
                    return True

        # checking diagonally
        for c in range(3, COLS):
            for r in range(3, ROWS):
                if game_board[r][c] == player_piece and game_board[r - 1][c - 1] == player_piece and game_board[r - 2][
                    c - 2] == player_piece and \
                        game_board[r - 3][c - 3] == player_piece:
                    return True

        return False

    @staticmethod
    def is_draw(game_board):
        return not np.any(game_board == 0)

    @staticmethod
    def score_position(game_board, piece):
        """
        compute the game board score for a given piece.
        you can change this function to use a better heuristic for improvement.
        """
        score = 0
        flag0 = flag1 = 0
        if BoardUtility.has_player_won(game_board, piece):
            return 100  # player has won the game give very large score
        if BoardUtility.has_player_won(game_board, 1 if piece == 2 else 2):
            return -100  # player has lost the game give very large negative score
        nextLocations = BoardUtility.get_valid_locations(game_board)
        for col in nextLocations:
            corresponding_row = BoardUtility.get_next_open_row(game_board, col)
            game_board[corresponding_row][col] = piece
            if BoardUtility.has_player_won(game_board, piece ): 
                game_board[corresponding_row][col] = 0
                score += 60
                break
            game_board[corresponding_row][col] = 0
        # else: flag0 = 1
            
        for col in nextLocations:
            corresponding_row = BoardUtility.get_next_open_row(game_board, col)
            game_board[corresponding_row][col] = 1 if piece == 2 else 2
            if BoardUtility.has_player_won(game_board, 1 if piece == 2 else 2):
                score -= 60
                break
            game_board[corresponding_row][col] = 0
        # else: flag1 = 1
        # if flag0 == 0 or flag1 == 0: 
        return score

        for col in range(COLS - 1):
            for row in range(ROWS - 1, 0, -1):
                if game_board[row][col] == 1:
                    if game_board[row][col+1] == 1:
                        score += 1
                    if game_board[row - 1][col + 1] == 1:
                        score += 1
                    if game_board[row - 1][col] == 1:
                        score += 1
                    elif game_board[row - 1][col] == 0:
                        break
                elif game_board[row][col] == 2:
                    if game_board[row][col+1] == 2:
                        score -= 1
                    if game_board[row - 1][col + 1] == 2:
                        score -= 1
                    if game_board[row - 1][col] == 2:
                        score -= 1
                    elif game_board[row - 1][col] == 0:
                        break
                else :
                    break
            if game_board[0][col] == 1:
                if game_board[0][col + 1] == 1:
                    score += 1
            if game_board[0][col] == 2:
                if game_board[0][col + 1] == 2:
                    score -= 1
        for row in range(ROWS - 1, 0, -1):
            if game_board[row - 1][COLS - 1] == 0:
                break
            if game_board[row][COLS - 1] == 1 and game_board[row - 1][COLS - 1] == 1:
                score += 1
            elif game_board[row][COLS - 1] == 2 and game_board[row - 1][COLS - 1] == 2:
                score -= 1
        return score if piece == 1 else -score

    @staticmethod
    def get_valid_locations(game_board):
        """
        returns all the valid columns to make a move.
        """
        valid_locations = []

        for column in range(COLS):
            if not BoardUtility.is_column_full(game_board, column):
                valid_locations.append(column)

        return valid_locations

    @staticmethod
    def is_terminal_state(game_board):
        """
        return True if either of the player have won the game or we have a draw.
        """
        return BoardUtility.has_player_won(game_board, 1) or BoardUtility.has_player_won(game_board,
                                                                                         2) or BoardUtility.is_draw(
            game_board)
