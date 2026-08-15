# Tic-Tac-Toe AI (Task 2 — CodSoft AI Internship)

An unbeatable Tic-Tac-Toe AI built in Python using the **Minimax algorithm
with Alpha-Beta Pruning**.

## Features
- Play against an AI that never loses (wins or draws every game).
- Choose to play as X or O.
- Clean terminal interface with numbered board positions (0–8).
- Alpha-Beta Pruning speeds up the search by skipping branches that
  can't affect the outcome.

## How the AI Works
1. **Minimax** explores every possible sequence of future moves from
   the current board state, building a game tree.
2. On the AI's turns it picks moves that **maximize** its score; on
   the human's turns it assumes they'll pick moves that **minimize**
   the AI's score (i.e., optimal defense).
3. **Alpha-Beta Pruning** keeps track of the best guaranteed scores
   for each side (`alpha`/`beta`) and cuts off branches once it's
   proven they can't change the final decision — same result, far
   fewer nodes explored.
4. Because Tic-Tac-Toe has a small, fully solvable search space, this
   guarantees **optimal play**: the AI can never be beaten, only
   drawn.