"""
Sudoku Solver GUI using Tkinter
Author: Yahav David Bragin
Date: June 25, 2025

This program provides a graphical user interface to input a Sudoku puzzle,
solve it using a backtracking algorithm (from `solver.py`), and display the solution.
"""

import tkinter as tk
from tkinter import messagebox
from solver import Solver


class SudokuUI:
    def __init__(self, master):
        """
        Initializes the main Sudoku UI.

        Args:
            master (tk.Tk): The root window.
        """
        self.master = master
        self.bg_color = "#1e1e1e"  # dark gray
        self.cell_bg = "#fdfdfd"
        self.highlight_color = "#00bfff"  # deep sky blue
        self.master.configure(bg=self.bg_color)
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.build_grid()
        self.build_controls()

    def build_grid(self):
        """
        Builds the 9x9 grid of Entry widgets for Sudoku input.
        """
        grid_frame = tk.Frame(self.master, bg=self.bg_color)
        grid_frame.grid(row=0, column=0, padx=20, pady=20)

        for i in range(9):
            for j in range(9):
                # Border thickness for 3x3 boxes
                top = 2 if i % 3 == 0 else 1
                left = 2 if j % 3 == 0 else 1
                bottom = 2 if i == 8 else 0
                right = 2 if j == 8 else 0

                entry = tk.Entry(
                    grid_frame,
                    width=2,
                    font=("Courier New", 20, "bold"),
                    justify="center",
                    bg=self.cell_bg,
                    fg="black",
                    insertbackground="red",
                    relief="flat",
                    highlightthickness=1,
                    highlightbackground="#555",
                    highlightcolor=self.highlight_color
                )

                entry.grid(row=i, column=j,
                           padx=(left, right),
                           pady=(top, bottom),
                           ipadx=13, ipady=12)
                entry.bind('<KeyRelease>', self.validate_entry)
                entry.bind('<FocusIn>', self.on_focus_in)
                entry.bind('<FocusOut>', self.on_focus_out)
                self.entries[i][j] = entry

    def build_controls(self):
        """
        Builds the "Solve" and "Clear" buttons below the grid.
        """
        controls_frame = tk.Frame(self.master, bg=self.bg_color)
        controls_frame.grid(row=1, column=0, pady=10)

        solve_button = tk.Button(
            controls_frame,
            text="Solve",
            command=self.solve,
            font=("Arial", 14, "bold"),
            bg="#4caf50",
            fg="black",
            activebackground="#45a049",
            activeforeground="white",
            relief="flat",
            padx=20,
            pady=5
        )
        solve_button.pack(side=tk.LEFT, padx=15)

        clear_button = tk.Button(
            controls_frame,
            text="Clear",
            command=self.clear_board,
            font=("Arial", 14, "bold"),
            bg="#f44336",
            fg="black",
            activebackground="#e53935",
            activeforeground="white",
            relief="flat",
            padx=20,
            pady=5
        )
        clear_button.pack(side=tk.LEFT, padx=15)

    def on_focus_in(self, event):
        """
        Highlights the entry when focused.
        """
        event.widget.configure(bg="#ffffcc")  # light yellow

    def on_focus_out(self, event):
        """
        Resets the entry background when focus is lost.
        """
        event.widget.configure(bg=self.cell_bg)

    def validate_entry(self, event):
        """
        Ensures only digits 1-9 are allowed in the entries.
        """
        widget = event.widget
        val = widget.get()
        if val not in list('123456789'):
            widget.delete(0, tk.END)

    def clear_board(self):
        """
        Clears all cells in the Sudoku grid.
        """
        for row in self.entries:
            for cell in row:
                cell.delete(0, tk.END)

    def get_board(self):
        """
        Reads the current board state from the entries.

        Returns:
            list[list[str]]: 9x9 list representing the current board.
        """
        return [
            [cell.get() for cell in row]
            for row in self.entries
        ]

    def set_board(self, board):
        """
        Fills the grid with the given board state.

        Args:
            board (list[list[str]]): 9x9 list with digits or '.' for empty cells.
        """
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                if board[i][j] != '.':
                    self.entries[i][j].insert(0, board[i][j])

    def solve(self):
        """
        Solves the Sudoku board and updates the GUI with the solution.
        """
        solver = Solver()
        board = self.get_board()
        print(board)  # optional: debug print
        if not solver.solve_sudoku(board):
            messagebox.showinfo("Sudoku Solver", "No solution found.")
        else:
            self.set_board(board)


def main():
    """
    Main entry point to run the Sudoku solver GUI.
    """
    root = tk.Tk()
    root.title("Sudoku Solver")
    root.configure(bg="#1e1e1e")
    root.resizable(False, False)
    SudokuUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
