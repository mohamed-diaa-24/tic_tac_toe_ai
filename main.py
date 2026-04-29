import tkinter as tk
from ui import TicTacToeUI


def main():
    root = tk.Tk()
    app = TicTacToeUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
