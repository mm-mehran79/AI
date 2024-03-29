import numpy as np
from Board import BoardUtility
import random


class Player:
    def __init__(self, player_piece):
        self.piece = player_piece

    def play(self, board):
        return 0


class RandomPlayer(Player):
    def play(self, board):
        return random.choice(BoardUtility.get_valid_locations(board))


class HumanPlayer(Player):
    def play(self, board):
        move = int(input("input the next column index 0 to 8:"))
        return move


class MiniMaxPlayer(Player):
    def __init__(self, player_piece, depth=5):
        super().__init__(player_piece)
        self.depth = depth

    def play(self, board):
        """
        Inputs : 
           board : 7*9 numpy array. 0 for empty cell, 1 and 2 for cells containig a piece.
        return the next move(columns to play in) of the player based on minimax algorithm.
        """
        # Todo: implement minimax algorithm with alpha beta pruning
        move = MiniMaxPlayer.MaxPlay(np.array(board), self.depth, -101, 101, self.piece, move=True)
        return move

    @staticmethod
    def MaxPlay(board, depth, alpha, beta, piece, move = False):
        value = -101
        nextMove = 0
        if BoardUtility.is_terminal_state(board) or depth == 0 :
            return BoardUtility.score_position(board, piece)
        else :
            for next_column in BoardUtility.get_valid_locations(board):
                #if alpha >= beta : break
                open_row = BoardUtility.get_next_open_row(board, next_column)
                board[open_row][next_column] = piece
                v = MiniMaxPlayer.MinPlay(board, depth - 1, alpha, beta, piece)
                board[open_row][next_column] = 0
                if v > value:
                    nextMove = next_column
                    value = v
                alpha = max(alpha, value)
                if beta <= value:
                    return next_column if move else v
        return nextMove if move else value
    @staticmethod
    def MinPlay(board, depth, alpha, beta, piece, move = False):
        value = 101
        nextMove = 0
        if BoardUtility.is_terminal_state(board) or depth == 0 :
            return BoardUtility.score_position(board, piece)
        else :
            for next_column in BoardUtility.get_valid_locations(board):
                #if alpha >= beta : break
                open_row = BoardUtility.get_next_open_row(board, next_column)
                board[open_row][next_column] = (1 if piece == 2 else 2)
                v = MiniMaxPlayer.MaxPlay(board, depth - 1, alpha, beta, piece)
                board[open_row][next_column] = 0
                if v < value:
                    nextMove = next_column
                    value = v
                beta = min(beta, v)
                if v <= alpha:
                    return next_column if move else v
        return nextMove if move else value


class MiniMaxProbPlayer(Player):
    def __init__(self, player_piece, depth=5, prob_stochastic=0.1):
        super().__init__(player_piece)
        self.depth = depth
        self.prob_stochastic = prob_stochastic

    def play(self, board):
        """
        Inputs : 
           board : 7*9 numpy array. 0 for empty cell, 1 and 2 for cells containig a piece.
        same as above but each time you are playing as max choose a random move instead of the best move
        with probability self.prob_stochastic.
        """
        # Todo: implement minimax algorithm with alpha beta pruning
        if np.random.rand() < self.prob_stochastic:
            move =  np.random.choice(BoardUtility.get_valid_locations(board))
        else :
            move = MiniMaxPlayer.MaxPlay(board, self.depth, -101, 101, self.piece, move=True)
        return move
