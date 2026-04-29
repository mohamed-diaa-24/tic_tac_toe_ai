import tkinter as tk
import tkinter.font as tkfont
from board import Board
from ai import AI


# ── Colour palette ──
BG_DARK      = "#0f0f1a"
BG_PANEL     = "#1a1a2e"
BG_CELL      = "#16213e"
BG_CELL_HOV  = "#1e2d4a"
ACCENT_TEAL  = "#00d4aa"
ACCENT_RED   = "#ff4757"
ACCENT_GOLD  = "#ffd32a"
TEXT_MAIN    = "#e8e8f0"
TEXT_DIM     = "#6c7a96"
BTN_RESTART  = "#2d3561"
BTN_RESTART_H= "#3d4771"


class TicTacToeUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Tic-Tac-Toe · AI Algorithms")
        self.root.configure(bg=BG_DARK)
        self.root.resizable(False, False)

        self.board = Board()
        self.ai = None
        self.game_over = False
        self.player_score = 0
        self.ai_score = 0
        self.draws = 0
        self.selected_algo = tk.StringVar(value="alphabeta")

        self._build_fonts()
        self._show_menu()

    def _build_fonts(self):
        self.f_title    = tkfont.Font(family="Courier", size=20, weight="bold")
        self.f_subtitle = tkfont.Font(family="Courier", size=11)
        self.f_cell     = tkfont.Font(family="Courier", size=28, weight="bold")
        self.f_status   = tkfont.Font(family="Courier", size=13, weight="bold")
        self.f_score    = tkfont.Font(family="Courier", size=11)
        self.f_btn      = tkfont.Font(family="Courier", size=11, weight="bold")
        self.f_menu_hdr = tkfont.Font(family="Courier", size=12, weight="bold")
        self.f_radio    = tkfont.Font(family="Courier", size=11)
        self.f_badge    = tkfont.Font(family="Courier", size=9, weight="bold")


    def _show_menu(self):
        for w in self.root.winfo_children():
            w.destroy()

        self.root.geometry("480x620")

        tk.Label(self.root, text="TIC-TAC-TOE", font=self.f_title,
                 fg=ACCENT_GOLD, bg=BG_DARK).pack(pady=(30, 2))
        tk.Label(self.root, text="A I   A L G O R I T H M S", font=self.f_subtitle,
                 fg=TEXT_DIM, bg=BG_DARK).pack(pady=(0, 25))

        card = tk.Frame(self.root, bg=BG_PANEL, bd=0, relief="flat")
        card.pack(expand=True,padx=40, fill="x")

        tk.Label(card, text="SELECT AI ALGORITHM", font=self.f_menu_hdr,
                 fg=ACCENT_TEAL, bg=BG_PANEL).pack(pady=(20, 10))

        algorithms = [
            (
                "alphabeta",
                "Alpha-Beta Pruning",
                ACCENT_TEAL,
            ),
            (
                "minimax",
                "Minimax",
                ACCENT_GOLD,
            ),
            (
                "greedy",
                "Greedy Heuristic",
                ACCENT_RED,
            ),
        ]

        for value, label, color in algorithms:
            row = tk.Frame(card, bg=BG_PANEL, cursor="hand2")
            row.pack(fill="x", padx=20, pady=5)

            rb = tk.Radiobutton(
                row,
                text=label,
                variable=self.selected_algo,
                value=value,
                font=self.f_menu_hdr,
                fg=color,
                bg=BG_PANEL,
                selectcolor=BG_DARK,
                activebackground=BG_PANEL,
                activeforeground=color,
                borderwidth=0,
                highlightthickness=0,
                cursor="hand2",
            )
            rb.pack(anchor="w")

        start_btn = tk.Button(
            self.root,
            text="START GAME  ▶",
            font=self.f_btn,
            fg=BG_DARK,
            bg=ACCENT_TEAL,
            activebackground="#00b894",
            activeforeground=BG_DARK,
            borderwidth=0,
            cursor="hand2",
            padx=30,
            pady=12,
            command=self._start_game,
        )
        start_btn.pack(side="bottom",pady=30)

        info = tk.Frame(self.root, bg=BG_DARK)
        info.pack(padx=40, fill="x")
        


    def _start_game(self):
        algo = self.selected_algo.get()
        self.ai = AI(algorithm=algo)
        self.board.reset()
        self.game_over = False
        self._build_game_ui()

    def _build_game_ui(self):
        for w in self.root.winfo_children():
            w.destroy()

        self.root.geometry("480x620")

        algo_names = {
            "minimax":   ("MINIMAX",         ACCENT_GOLD),
            "alphabeta": ("ALPHA-BETA",       ACCENT_TEAL),
            "greedy":    ("GREEDY HEURISTIC", ACCENT_RED),
        }
        algo_label, algo_color = algo_names[self.ai.algorithm]

        hdr = tk.Frame(self.root, bg=BG_DARK)
        hdr.pack(fill="x", padx=24, pady=(20, 0))

        tk.Label(hdr, text="TIC-TAC-TOE", font=self.f_title,
                 fg=TEXT_MAIN, bg=BG_DARK).pack(side="left")

        badge = tk.Label(hdr, text=algo_label, font=self.f_badge,
                         fg=BG_DARK, bg=algo_color, padx=8, pady=4)
        badge.pack(side="right", pady=8)

        score_bar = tk.Frame(self.root, bg=BG_PANEL)
        score_bar.pack(fill="x", padx=24, pady=10)

        self.lbl_player_score = tk.Label(
            score_bar, text=f"YOU\n{self.player_score}",
            font=self.f_menu_hdr, fg=ACCENT_TEAL, bg=BG_PANEL, padx=20, pady=8)
        self.lbl_player_score.pack(side="left", expand=True)

        self.lbl_draws = tk.Label(
            score_bar, text=f"DRAW\n{self.draws}",
            font=self.f_menu_hdr, fg=TEXT_DIM, bg=BG_PANEL, padx=20, pady=8)
        self.lbl_draws.pack(side="left", expand=True)

        self.lbl_ai_score = tk.Label(
            score_bar, text=f"AI\n{self.ai_score}",
            font=self.f_menu_hdr, fg=ACCENT_RED, bg=BG_PANEL, padx=20, pady=8)
        self.lbl_ai_score.pack(side="left", expand=True)

        board_frame = tk.Frame(self.root, bg=BG_DARK)
        board_frame.pack(padx=24, pady=5)

        self.buttons: list[tk.Button] = []
        for i in range(9):
            btn = tk.Button(
                board_frame,
                text="",
                font=self.f_cell,
                width=4,
                height=2,
                bg=BG_CELL,
                fg=TEXT_MAIN,
                activebackground=BG_CELL_HOV,
                activeforeground=TEXT_MAIN,
                disabledforeground=TEXT_MAIN,
                borderwidth=0,
                highlightthickness=1,
                highlightbackground=BG_PANEL,
                cursor="hand2",
                command=lambda idx=i: self._on_click(idx),
            )
            btn.grid(row=i // 3, column=i % 3, padx=4, pady=4)
            self.buttons.append(btn)

        self.lbl_status = tk.Label(
            self.root,
            text="Your turn  (X)",
            font=self.f_status,
            fg=ACCENT_GOLD,
            bg=BG_DARK,
        )
        self.lbl_status.pack(pady=12)

        btn_row = tk.Frame(self.root, bg=BG_DARK)
        btn_row.pack(pady=5)

        tk.Button(
            btn_row, text="↺  RESTART", font=self.f_btn,
            fg=TEXT_MAIN, bg=BTN_RESTART,
            activebackground=BTN_RESTART_H, activeforeground=TEXT_MAIN,
            borderwidth=0, cursor="hand2", padx=16, pady=8,
            command=self._restart,
        ).pack(side="left", padx=6)

        tk.Button(
            btn_row, text="⬅  MENU", font=self.f_btn,
            fg=TEXT_DIM, bg=BG_PANEL,
            activebackground=BG_CELL, activeforeground=TEXT_MAIN,
            borderwidth=0, cursor="hand2", padx=16, pady=8,
            command=self._go_to_menu,
        ).pack(side="left", padx=6)

    # GAME LOGIC HANDLERS

    def _on_click(self, index: int):
        if self.game_over:
            return

        if self.board.make_move(index, "X"):
            self.buttons[index].config(text="X", fg=ACCENT_TEAL,
                                       disabledforeground=ACCENT_TEAL,
                                       state="disabled")
            if self._check_end("X"):
                return

            self.lbl_status.config(text="AI is thinking…", fg=TEXT_DIM)
            self.root.after(350, self._ai_turn)

    def _ai_turn(self):
        if self.game_over:
            return

        move = self.ai.get_move(self.board)
        if move is not None:
            self.board.make_move(move, "O")
            self.buttons[move].config(text="O", fg=ACCENT_RED,
                                      disabledforeground=ACCENT_RED,
                                      state="disabled")
            if self._check_end("O"):
                return

        self.lbl_status.config(text="Your turn  (X)", fg=ACCENT_GOLD)

    def _check_end(self, player: str) -> bool:
        if self.board.check_winner(player):
            winning_combo = self.board.get_winning_line(player)
            self._highlight_winner(winning_combo, player)

            if player == "X":
                self.player_score += 1
                self.lbl_status.config(text="🎉  You win!", fg=ACCENT_TEAL)
                self.lbl_player_score.config(text=f"YOU\n{self.player_score}")
            else:
                self.ai_score += 1
                self.lbl_status.config(text="💀  AI wins!", fg=ACCENT_RED)
                self.lbl_ai_score.config(text=f"AI\n{self.ai_score}")

            self.game_over = True
            self._disable_all()
            return True

        if self.board.is_draw():
            self.draws += 1
            self.lbl_status.config(text="It's a draw!", fg=TEXT_DIM)
            self.lbl_draws.config(text=f"DRAW\n{self.draws}")
            self.game_over = True
            return True

        return False

    def _highlight_winner(self, combo: tuple, player: str):
        if combo is None:
            return
        color = ACCENT_TEAL if player == "X" else ACCENT_RED
        for idx in combo:
            self.buttons[idx].config(bg=color, fg=BG_DARK,
                                     disabledforeground=BG_DARK)

    def _disable_all(self):
        for btn in self.buttons:
            btn.config(state="disabled")

    def _restart(self):
        self.board.reset()
        self.game_over = False
        for btn in self.buttons:
            btn.config(text="", state="normal", bg=BG_CELL,
                       fg=TEXT_MAIN, disabledforeground=TEXT_MAIN)
        self.lbl_status.config(text="Your turn  (X)", fg=ACCENT_GOLD)

    def _go_to_menu(self):
        self.player_score = 0
        self.ai_score = 0
        self.draws = 0
        self._show_menu()