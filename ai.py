import math
import random
from board import Board


class AI:
    HEURISTIC_SCORES = {
        ("O", "O", ""):  100,
        ("O", "", "O"):  100,
        ("", "O", "O"):  100,
        ("X", "X", ""):  -80,
        ("X", "", "X"):  -80,
        ("", "X", "X"):  -80,
        ("O", "", ""):    10,
        ("", "O", ""):    10,
        ("", "", "O"):    10,
        ("X", "", ""):    -5,
        ("", "X", ""):    -5,
        ("", "", "X"):    -5,
    }

    def __init__(self, algorithm: str = "alphabeta"):
        self.algorithm = algorithm
        self.ai_mark = "O"
        self.human_mark = "X"

    def get_move(self, board: Board) -> int:
        if self.algorithm == "minimax":
            return self._minimax_move(board)
        elif self.algorithm == "alphabeta":
            return self._alphabeta_move(board)
        elif self.algorithm == "greedy":
            return self._greedy_move(board)
        else:
            raise ValueError(f"Unknown algorithm: {self.algorithm}")


    def _minimax_move(self, board: Board) -> int:
        best_score = -math.inf
        best_move = None

        for move in board.get_empty_cells():
            board.make_move(move, self.ai_mark)
            score = self._minimax(board, is_maximizing=False)
            board.undo_move(move)

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def _minimax(self, board: Board, is_maximizing: bool) -> int:
        if board.check_winner(self.ai_mark):
            return 1
        if board.check_winner(self.human_mark):
            return -1
        if board.is_draw():
            return 0

        if is_maximizing:
            best_score = -math.inf
            for move in board.get_empty_cells():
                board.make_move(move, self.ai_mark)
                score = self._minimax(board, is_maximizing=False)
                board.undo_move(move)
                best_score = max(best_score, score)
            return best_score
        else:
            best_score = math.inf
            for move in board.get_empty_cells():
                board.make_move(move, self.human_mark)
                score = self._minimax(board, is_maximizing=True)
                board.undo_move(move)
                best_score = min(best_score, score)
            return best_score


    def _alphabeta_move(self, board: Board) -> int:
        best_score = -math.inf
        best_move = None

        for move in board.get_empty_cells():
            board.make_move(move, self.ai_mark)
            score = self._alphabeta(board, is_maximizing=False,
                                    alpha=-math.inf, beta=math.inf)
            board.undo_move(move)

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def _alphabeta(self, board: Board, is_maximizing: bool,
                   alpha: float, beta: float) -> int:
        if board.check_winner(self.ai_mark):
            return 1
        if board.check_winner(self.human_mark):
            return -1
        if board.is_draw():
            return 0

        if is_maximizing:
            best_score = -math.inf
            for move in board.get_empty_cells():
                board.make_move(move, self.ai_mark)
                score = self._alphabeta(board, False, alpha, beta)
                board.undo_move(move)
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)

                if beta <= alpha:
                    break  

            return best_score
        else:
            best_score = math.inf
            for move in board.get_empty_cells():
                board.make_move(move, self.human_mark)
                score = self._alphabeta(board, True, alpha, beta)
                board.undo_move(move)
                best_score = min(best_score, score)
                beta = min(beta, best_score)

                if beta <= alpha:
                    break  

            return best_score

    def _greedy_move(self, board: Board) -> int:

        best_score = -math.inf
        best_moves = []

        for move in board.get_empty_cells():
            board.make_move(move, self.ai_mark)
            score = self._evaluate_board(board)
            board.undo_move(move)

            if score > best_score:
                best_score = score
                best_moves = [move]
            elif score == best_score:
                best_moves.append(move)

        return random.choice(best_moves)

    def _evaluate_board(self, board: Board) -> int:
        total_score = 0
        for combo in Board.WIN_COMBINATIONS:
            line = tuple(board.cells[i] for i in combo)
            total_score += self.HEURISTIC_SCORES.get(line, 0)
        return total_score
