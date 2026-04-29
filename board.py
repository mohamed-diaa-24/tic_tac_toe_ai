class Board:

    WIN_COMBINATIONS = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    def __init__(self):
        self.cells = [""] * 9

    def reset(self):
        self.cells = [""] * 9

    def make_move(self, index: int, player: str) -> bool:
        if self.cells[index] == "":
            self.cells[index] = player
            return True
        return False

    def undo_move(self, index: int):

        self.cells[index] = ""

    def get_empty_cells(self) -> list[int]:
        return [i for i in range(9) if self.cells[i] == ""]

    def check_winner(self, player: str) -> bool:

        for a, b, c in self.WIN_COMBINATIONS:
            if self.cells[a] == self.cells[b] == self.cells[c] == player:
                return True
        return False

    def get_winning_line(self, player: str) -> tuple | None:

        for combo in self.WIN_COMBINATIONS:
            a, b, c = combo
            if self.cells[a] == self.cells[b] == self.cells[c] == player:
                return combo
        return None

    def is_draw(self) -> bool:
        return "" not in self.cells

    def is_game_over(self) -> bool:
        return self.check_winner("X") or self.check_winner("O") or self.is_draw()
