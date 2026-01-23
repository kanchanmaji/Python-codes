# tic_tac_toe.py
# Tic-Tac-Toe with Tkinter GUI and optional Minimax AI (perfect play).
# Works in Pydroid 3 (save and run script).

import tkinter as tk
from tkinter import messagebox

# --- Game logic utilities ---

def check_winner(board):
    """Return 'X' or 'O' if there's a winner, 'Draw' if board full, or None otherwise.
       board: list of 9 elements, each 'X', 'O', or None.
    """
    wins = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # cols
        (0,4,8), (2,4,6)            # diagonals
    ]
    for a,b,c in wins:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    if all(cell is not None for cell in board):
        return 'Draw'
    return None

def available_moves(board):
    return [i for i,cell in enumerate(board) if cell is None]

# Minimax AI for perfect play
def minimax(board, player, ai_player, human_player):
    """Return (score, move_index). Score: +1 win for ai, -1 loss, 0 draw."""
    winner = check_winner(board)
    if winner == ai_player:
        return (1, None)
    elif winner == human_player:
        return (-1, None)
    elif winner == 'Draw':
        return (0, None)

    moves = available_moves(board)
    if player == ai_player:
        best_score = -2
        best_move = None
        for m in moves:
            board[m] = player
            score, _ = minimax(board, human_player, ai_player, human_player)
            board[m] = None
            if score > best_score:
                best_score = score
                best_move = m
                if best_score == 1:
                    break
        return (best_score, best_move)
    else:
        worst_score = 2
        worst_move = None
        for m in moves:
            board[m] = player
            score, _ = minimax(board, ai_player, ai_player, human_player)
            board[m] = None
            if score < worst_score:
                worst_score = score
                worst_move = m
                if worst_score == -1:
                    break
        return (worst_score, worst_move)

# --- GUI and main program ---

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        root.title("Tic Tac Toe — Pydroid 3 / Tkinter")
        self.board = [None]*9
        self.current_player = 'X'   # X always starts
        self.scores = {'X': 0, 'O': 0, 'Draw': 0}
        self.mode = tk.StringVar(value='two')  # 'two' or 'single'
        self.ai_starts = tk.BooleanVar(value=False)

        # Top frame: mode selection & controls
        top = tk.Frame(root)
        top.pack(padx=10, pady=6)

        tk.Label(top, text="Mode:").grid(row=0, column=0, sticky='w')
        tk.Radiobutton(top, text="Two Players", variable=self.mode, value='two').grid(row=0, column=1)
        tk.Radiobutton(top, text="Single Player (vs CPU)", variable=self.mode, value='single').grid(row=0, column=2)
        tk.Checkbutton(top, text="CPU starts (O)", variable=self.ai_starts).grid(row=0, column=3, padx=6)

        tk.Button(top, text="New Game", command=self.new_game).grid(row=0, column=4, padx=6)
        tk.Button(top, text="Reset Score", command=self.reset_score).grid(row=0, column=5, padx=6)

        # Middle frame: board
        board_frame = tk.Frame(root)
        board_frame.pack(padx=10, pady=6)
        self.buttons = []
        for i in range(9):
            b = tk.Button(board_frame, text='', font=('Helvetica', 14), width=3, height=2,
                          command=lambda i=i: self.on_click(i))
            b.grid(row=i//3, column=i%3, padx=4, pady=4)
            self.buttons.append(b)

        # Bottom: status and scores
        bottom = tk.Frame(root)
        bottom.pack(padx=10, pady=6, fill='x')
        self.status_label = tk.Label(bottom, text="Turn: X", font=('Helvetica', 14))
        self.status_label.pack(side='left')
        self.score_label = tk.Label(bottom, text=self.score_text(), font=('Helvetica', 12))
        self.score_label.pack(side='right')

        # If single-player and CPU should start, let it make a move
        self.new_game(initial=True)

    def score_text(self):
        return f"Scores — X: {self.scores['X']}   O: {self.scores['O']}   Draws: {self.scores['Draw']}"

    def new_game(self, initial=False):
        self.board = [None]*9
        self.current_player = 'X'
        for b in self.buttons:
            b.config(text='', state='normal')
        self.status_label.config(text=f"Turn: {self.current_player}")
        if self.mode.get() == 'single' and self.ai_starts.get() and not initial:
            # If user changed mode mid-session and asked new game, let CPU (O) start by playing O
            self.root.after(200, self.cpu_move)  # slight delay so UI updates
        elif self.mode.get() == 'single' and self.ai_starts.get() and initial:
            # when program starts and ai_starts True, CPU should play first
            self.root.after(200, self.cpu_move)

    def reset_score(self):
        self.scores = {'X': 0, 'O': 0, 'Draw': 0}
        self.score_label.config(text=self.score_text())

    def on_click(self, index):
        if self.board[index] is not None:
            return
        if self.mode.get() == 'single' and self.current_player == 'O':
            # If it's CPU's turn, ignore clicks
            return

        self.make_move(index, self.current_player)
        result = check_winner(self.board)
        if result:
            self.handle_result(result)
            return

        # Switch player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.status_label.config(text=f"Turn: {self.current_player}")

        # If single-player and now it's CPU's turn, let CPU play
        if self.mode.get() == 'single' and self.current_player == 'O':
            self.root.after(200, self.cpu_move)

    def make_move(self, index, player):
        self.board[index] = player
        self.buttons[index].config(text=player)
        # disable button to avoid accidental double clicks
        self.buttons[index].config(state='disabled')

    def cpu_move(self):
        # CPU plays as 'O' (by our design). Uses minimax against 'X'.
        ai_player = 'O'
        human_player = 'X'
        # If board empty and CPU wants to start, choose center for efficiency
        if all(cell is None for cell in self.board):
            preferred = 4  # center
            self.make_move(preferred, ai_player)
        else:
            _, move = minimax(self.board, ai_player, ai_player, human_player)
            if move is None:
                # No move (shouldn't happen if called correctly)
                moves = available_moves(self.board)
                if not moves:
                    return
                move = moves[0]
            self.make_move(move, ai_player)

        result = check_winner(self.board)
        if result:
            self.handle_result(result)
            return

        # Back to player X
        self.current_player = 'X'
        self.status_label.config(text=f"Turn: {self.current_player}")

    def handle_result(self, result):
        if result in ('X', 'O'):
            message = f"{result} wins!"
            self.scores[result] += 1
        else:
            message = "It's a draw!"
            self.scores['Draw'] += 1

        # disable all buttons
        for b in self.buttons:
            b.config(state='disabled')

        self.score_label.config(text=self.score_text())
        self.status_label.config(text=message)
        # Offer quick new game popup
        # Using a non-blocking small info box; users can press New Game to continue.
        # But also provide a messagebox choice to start anew.
        ans = messagebox.askyesno("Game Over", f"{message}\n\nStart a new game?")
        if ans:
            # If CPU should start and mode single and ai_starts True, set current player accordingly
            if self.mode.get() == 'single' and self.ai_starts.get():
                # Make sure CPU plays first as O
                self.new_game()
                # Let CPU move after small delay
                self.root.after(200, self.cpu_move)
            else:
                self.new_game()

def main():
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()