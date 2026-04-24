import game_logic as gl


def minimax(board, is_maximizing):
    """
    Minimax algorithm:
    - AI    = "O" → maximizer (wants +1)
    - Human = "X" → minimizer (wants -1)
    """
    if _check_winner_board(board, "O"):
        return 1
    if _check_winner_board(board, "X"):
        return -1
    if "" not in board:
        return 0  # draw

    if is_maximizing:
        best = -float("inf")
        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = ""
                best = max(best, score)
        return best
    else:
        best = float("inf")
        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = ""
                best = min(best, score)
        return best


def _check_winner_board(board, player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def get_ai_move():
    """Return the best move index for the AI using Minimax."""
    board = gl.board[:]  # work on a copy
    best_score = -float("inf")
    best_move = None

    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                best_move = i

    return best_move
