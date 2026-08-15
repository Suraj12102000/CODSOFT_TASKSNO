import math
import os
import random


class TicTacToe:

    def __init__(self):
        # Board positions are indexed 0-8:
        #  0 | 1 | 2
        #  ---------
        #  3 | 4 | 5
        #  ---------
        #  6 | 7 | 8
        self.board = [" "] * 9

    def available_moves(self):
        """Return list of empty cell indices."""
        return [i for i, cell in enumerate(self.board) if cell == " "]

    def make_move(self, position, player):
        """Place a player's mark on the board if the cell is empty."""
        if self.board[position] == " ":
            self.board[position] = player
            return True
        return False

    def undo_move(self, position):
        """Undo a move (used by Minimax to backtrack)."""
        self.board[position] = " "

    WIN_LINES = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),   
        (0, 3, 6), (1, 4, 7), (2, 5, 8),   
        (0, 4, 8), (2, 4, 6),              
    ]

    def winner(self):
        for a, b, c in self.WIN_LINES:
            if self.board[a] != " " and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        return None

    def is_full(self):
        return " " not in self.board

    def is_game_over(self):
        return self.winner() is not None or self.is_full()

    def print_board(self):
        symbols = [c if c != " " else str(i) for i, c in enumerate(self.board)]
        print()
        print(f"  {symbols[0]} | {symbols[1]} | {symbols[2]}")
        print(" ---+---+---")
        print(f"  {symbols[3]} | {symbols[4]} | {symbols[5]}")
        print(" ---+---+---")
        print(f"  {symbols[6]} | {symbols[7]} | {symbols[8]}")
        print()


class MinimaxAI:
    def __init__(self, ai_player="O", human_player="X"):
        self.ai_player = ai_player
        self.human_player = human_player

    def score(self, game, depth):
        win = game.winner()
        if win == self.ai_player:
            return 10 - depth
        elif win == self.human_player:
            return depth - 10
        return 0

    def minimax(self, game, depth, is_maximizing, alpha, beta):
        if game.is_game_over():
            return self.score(game, depth)

        if is_maximizing:
            best_score = -math.inf
            for move in game.available_moves():
                game.make_move(move, self.ai_player)
                current = self.minimax(game, depth + 1, False, alpha, beta)
                game.undo_move(move)
                best_score = max(best_score, current)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break  # Beta cutoff - prune remaining branches
            return best_score
        else:
            best_score = math.inf
            for move in game.available_moves():
                game.make_move(move, self.human_player)
                current = self.minimax(game, depth + 1, True, alpha, beta)
                game.undo_move(move)
                best_score = min(best_score, current)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break  # Alpha cutoff - prune remaining branches
            return best_score

    def best_move(self, game):
        best_score = -math.inf
        move_choice = None

        moves = game.available_moves()
        random.shuffle(moves)

        for move in moves:
            game.make_move(move, self.ai_player)
            move_score = self.minimax(game, 0, False, -math.inf, math.inf)
            game.undo_move(move)

            if move_score > best_score:
                best_score = move_score
                move_choice = move

        return move_choice


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_human_move(game, human_player):
    while True:
        raw = input(f"Player '{human_player}', enter your move (0-8): ").strip()
        if not raw.isdigit():
            print("Please enter a number between 0 and 8.")
            continue
        pos = int(raw)
        if pos not in range(9):
            print("Please enter a number between 0 and 8.")
            continue
        if game.board[pos] != " ":
            print("That cell is already taken. Choose another.")
            continue
        return pos


def choose_symbol():
    while True:
        choice = input("Do you want to play as X or O? (X goes first): ").strip().upper()
        if choice in ("X", "O"):
            return choice
        print("Please type X or O.")


def play_game():
    print("=" * 50)
    print("        TIC-TAC-TOE — Unbeatable AI")
    print("   (Minimax with Alpha-Beta Pruning)")
    print("=" * 50)
    print("Cells are numbered 0-8 as shown below:\n")
    print("  0 | 1 | 2\n ---+---+---\n  3 | 4 | 5\n ---+---+---\n  6 | 7 | 8\n")

    human_player = choose_symbol()
    ai_player = "O" if human_player == "X" else "X"
    ai = MinimaxAI(ai_player=ai_player, human_player=human_player)

    game = TicTacToe()
    current_turn = "X"  

    game.print_board()

    while not game.is_game_over():
        if current_turn == human_player:
            pos = get_human_move(game, human_player)
            game.make_move(pos, human_player)
        else:
            print(f"AI ('{ai_player}') is thinking...")
            pos = ai.best_move(game)
            game.make_move(pos, ai_player)
            print(f"AI played position {pos}.")

        game.print_board()
        current_turn = "O" if current_turn == "X" else "X"

    winner = game.winner()
    if winner == human_player:
        print("🎉 Congratulations, you won! (This shouldn't be possible... nice glitch!)")
    elif winner == ai_player:
        print("🤖 The AI wins! Better luck next time.")
    else:
        print("🤝 It's a draw! Optimal play from both sides.")


if __name__ == "__main__":
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break
        clear_screen()
