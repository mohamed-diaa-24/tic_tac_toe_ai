# 🎮 Tic Tac Toe AI

A desktop Tic Tac Toe game built with Python and Tkinter, featuring an unbeatable AI opponent powered by the **Minimax algorithm**.

---

## 📸 Overview

Play the classic 3×3 Tic Tac Toe against an AI that never loses. The AI evaluates every possible future move and always picks the optimal one — the best you can do is a draw!

---

## 🗂️ Project Structure

```
tic_tac_toe_ai/
├── main.py           # Entry point — launches the app
├── ui.py             # Tkinter GUI (board, buttons, scoreboard)
├── game_logic.py     # Board state, move validation, win/draw detection
└── ai.py             # Minimax AI algorithm
```

---

## ⚙️ How It Works

### Game Logic (`game_logic.py`)
- Manages the board as a list of 9 cells (`""`, `"X"`, or `"O"`)
- `make_move(index, player)` — places a mark if the cell is empty
- `check_winner(player)` — checks all 8 winning combinations
- `is_draw()` — returns `True` when the board is full with no winner
- `reset_board()` — resets the board for a new game

### AI — Minimax (`ai.py`)
The AI uses the **Minimax algorithm**, a decision-making strategy used in two-player zero-sum games.

- The AI plays as `"O"` (maximizer — tries to get score `+1`)
- The human plays as `"X"` (minimizer — tries to get score `-1`)
- A draw scores `0`

At every turn, the AI simulates all possible future game states and picks the move that **guarantees the best outcome**, making it mathematically unbeatable.

```
get_ai_move()
  └── tries every empty cell
        └── minimax(board, is_maximizing)
              ├── base case: win → +1 / lose → -1 / draw → 0
              ├── maximizing (AI turn)  → picks highest score
              └── minimizing (human turn) → picks lowest score
```

### UI (`ui.py`)
- Dark-themed Tkinter interface (`#2b2b36` background)
- 3×3 clickable grid — human clicks to place `X`
- AI responds automatically after a 400ms delay
- Live scoreboard tracking Player vs AI wins
- Color-coded marks: `X` in green, `O` in red
- Restart button to reset the board without losing the score

---

## 🚀 Getting Started

### Requirements
- Python 3.x
- Tkinter (included with standard Python installations)

### Run the game
```bash
python main.py
```

---

## 🎯 How to Play

| Action | Description |
|--------|-------------|
| Click a cell | Place your mark (`X`) |
| Wait | AI responds automatically as `O` |
| Restart Game | Resets the board, keeps the score |

---

## 🧠 Why Minimax?

Minimax is a classic AI algorithm for perfect-information games. In Tic Tac Toe (which has only 9 cells), the AI can explore the **entire game tree** in milliseconds, guaranteeing the optimal move every time. This means:

- If you play perfectly → **Draw**
- If you make a mistake → **AI wins**
- The AI will **never lose**

---

## 📄 License

This project is open source and free to use for educational purposes.
