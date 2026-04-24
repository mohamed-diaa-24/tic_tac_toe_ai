import tkinter as tk
import tkinter.font as tkfont
import game_logic as gl
import ai


class TicTacToeUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe AI")
        self.root.geometry("400x550")
        self.root.configure(bg="#2b2b36") # Modern dark background
        self.root.resizable(False, False)

        self.player_score = 0
        self.ai_score = 0
        self.game_over = False

        self.create_ui()

    def create_ui(self):
        # Fonts
        title_font = tkfont.Font(family="Helvetica", size=24, weight="bold")
        self.btn_font = tkfont.Font(family="Helvetica", size=24, weight="bold")
        status_font = tkfont.Font(family="Helvetica", size=16, weight="bold")
        score_font = tkfont.Font(family="Helvetica", size=14, weight="bold")
        restart_font = tkfont.Font(family="Helvetica", size=14, weight="bold")

        # Title
        tk.Label(
            self.root,
            text="Tic Tac Toe AI",
            font=title_font,
            fg="#00d2d3",
            bg="#2b2b36"
        ).pack(pady=(20, 10))

        # Score Board Frame
        score_frame = tk.Frame(self.root, bg="#2b2b36")
        score_frame.pack(pady=5)

        self.score = tk.Label(
            score_frame,
            text="Player: 0  |  AI: 0",
            font=score_font,
            fg="#c8d6e5",
            bg="#2b2b36"
        )
        self.score.pack()

        # Board
        self.frame = tk.Frame(self.root, bg="#2b2b36")
        self.frame.pack(pady=15)

        self.buttons = []

        for i in range(9):
            btn = tk.Button(
                self.frame,
                text="",
                font=self.btn_font,
                width=4,
                height=2,
                bg="#3d3d4e", # slightly lighter background for buttons
                activebackground="#4a4a5e",
                fg="white",
                borderwidth=0,
                cursor="hand2",
                command=lambda i=i: self.click(i)
            )
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(btn)

        # Status
        self.status = tk.Label(
            self.root,
            text="Your Turn (X)",
            font=status_font,
            fg="#ff9f43",
            bg="#2b2b36"
        )
        self.status.pack(pady=10)

        # Restart Button
        restart_btn = tk.Button(
            self.root,
            text="Restart Game",
            font=restart_font,
            bg="#ff6b6b",
            fg="white",
            activebackground="#ee5253",
            activeforeground="white",
            borderwidth=0,
            cursor="hand2",
            padx=20,
            pady=10,
            command=self.restart
        )
        restart_btn.pack(pady=10)

    def click(self, i):
        if self.game_over:
            return

        if gl.make_move(i, "X"):
            self.buttons[i].config(text="X", fg="#1dd1a1", disabledforeground="#1dd1a1", state="disabled")

            if gl.check_winner("X"):
                self.status.config(text="You Win!", fg="#1dd1a1")
                self.player_score += 1
                self.update_score()
                self.game_over = True
                self.disable()
                return

            if gl.is_draw():
                self.status.config(text="It's a Draw!", fg="#c8d6e5")
                self.game_over = True
                return

            self.status.config(text="AI is waiting...", fg="#54a0ff")
            self.root.after(400, self.ai_turn)

    def ai_turn(self):
        if self.game_over:
            return

        move = ai.get_ai_move()

        if move is not None:
            gl.make_move(move, "O")
            self.buttons[move].config(text="O", fg="#ff6b6b", disabledforeground="#ff6b6b", state="disabled")

            if gl.check_winner("O"):
                self.status.config(text="💀 AI Wins!", fg="#ff6b6b")
                self.ai_score += 1
                self.update_score()
                self.game_over = True
                self.disable()
                return

            if gl.is_draw():
                self.status.config(text="It's a Draw!", fg="#c8d6e5")
                self.game_over = True
                return

            self.status.config(text="Your Turn (X)", fg="#ff9f43")

    def update_score(self):
        self.score.config(
            text=f"Player: {self.player_score}  |  AI: {self.ai_score}"
        )

    def disable(self):
        for b in self.buttons:
            b.config(state="disabled")

    def restart(self):
        gl.reset_board()
        self.game_over = False

        for b in self.buttons:
            b.config(text="", state="normal", bg="#3d3d4e")

        self.status.config(text="Your Turn (X)", fg="#ff9f43")