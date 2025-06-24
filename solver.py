"""
Sudoku Solver Logic (Backtracking Algorithm)
Author: Yahav David Bragin
Date: June 25, 2025

This module defines the Solver class, which can solve a standard 9x9 Sudoku puzzle
using a recursive backtracking method.
"""

from typing import Optional


class Solver:
    def solve_sudoku(self, board: list[list[str]]) -> bool:
        """
        Attempts to solve the given Sudoku board in-place using backtracking.

        Args:
            board (list[list[str]]): A 9x9 Sudoku board, with empty cells as ''.

        Returns:
            bool: True if a valid solution was found, False otherwise.
        """
        cell = self.find_empty(board)
        if cell is None:
            return True  # No empty cells left — puzzle is solved

        row, col = cell
        for digit in map(str, range(1, 10)):
            if self.is_valid(board, row, col, digit):
                board[row][col] = digit
                if self.solve_sudoku(board):
                    return True
                board[row][col] = ''  # Backtrack

        return False  # Trigger backtracking

    def is_valid(self, board: list[list[str]], row: int, col: int, digit: str) -> bool:
        """
        Checks whether placing a digit in the specified cell is valid
        according to Sudoku rules.

        Args:
            board (list[list[str]]): Sudoku board.
            row (int): Row index of the cell.
            col (int): Column index of the cell.
            digit (str): The digit to validate (as a string '1'-'9').

        Returns:
            bool: True if the digit can be legally placed, False otherwise.
        """
        # Check row and column
        for i in range(9):
            if board[row][i] == digit or board[i][col] == digit:
                return False

        # Check 3x3 subgrid
        top_row = (row // 3) * 3
        top_col = (col // 3) * 3
        for i in range(top_row, top_row + 3):
            for j in range(top_col, top_col + 3):
                if board[i][j] == digit:
                    return False

        return True

    def find_empty(self, board: list[list[str]]) -> Optional[tuple[int, int]]:
        """
        Finds the next empty cell in the Sudoku board.

        Args:
            board (list[list[str]]): Sudoku board.

        Returns:
            Optional[tuple[int, int]]: The (row, col) of the first empty cell found,
            or None if the board is full.
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == '':
                    return i, j
        return None
