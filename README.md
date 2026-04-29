# 🎮 Tic Tac Toe AI

A desktop Tic Tac Toe game built with Python and Tkinter, featuring an unbeatable AI opponent powered by the **3 AI Algorithms**.

---

## 📸 Overview

Play the classic 3×3 Tic Tac Toe against an AI that never loses. The AI evaluates every possible future move and always picks the optimal one — the best you can do is a draw!

---

## 🗂️ Project Structure

```
tic_tac_toe_ai/
├── main.py           # Entry point — launches the app
├── ui.py             # Tkinter GUI (board, buttons, scoreboard)
├── board.py          # Board state, move validation, win/draw detection
└── ai.py             # Minimax AI algorithm
```

---

## ⚙️ How It Works

### Game Logic (`board.py`)

- Manages the board as a list of 9 cells (`""`, `"X"`, or `"O"`)
- `make_move(index, player)` — places a mark if the cell is empty
- `check_winner(player)` — checks all 8 winning combinations
- `is_draw()` — returns `True` when the board is full with no winner
- `reset_board()` — resets the board for a new game

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

## How It Works (The 3 AI Algorithms)

### 1. Minimax

The standard recursive algorithm for perfect play. It explores the entire game tree to ensure the AI never loses.

- **Goal:** Maximize the AI's score and minimize the player's score.
- **Outcome:** Guaranteed draw or win.

---

### 2. Alpha-Beta Pruning

An enhanced version of Minimax that improves performance.

- **How:** It uses two variables, $\alpha$ (best already explored option for maximizer) and $\beta$ (best for minimizer). If a branch is found to be worse than a previously examined one, it _prunes_ (stops searching) that branch.
- **Result:** Same "perfect" moves as Minimax but with faster computation.

---

### 3. Greedy Algorithm

A more "short-sighted" approach compared to the others.

- **How:** It evaluates the board based on the immediate next turn. It prioritizes:
  1. Winning in one move
  2. Blocking the opponent
  3. Taking the center or corners
- **Result:** Very fast, but potentially beatable by experienced players!

---

## 🎯 How to Play

| Action       | Description                       |
| ------------ | --------------------------------- |
| Click a cell | Place your mark (`X`)             |
| Wait         | AI responds automatically as `O`  |
| Restart Game | Resets the board, keeps the score |

---

## 📄 License

This project is open source and free to use for educational purposes.
