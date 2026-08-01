#!/usr/bin/python3
"""Solve the N queens puzzle and print every solution.

Usage:
    ./101-nqueens.py N
"""
import sys


def is_safe(board, row, col):
    """Check if a queen can be placed at (row, col) safely.

    Args:
        board (list): The current partial solution, board[r] = c.
        row (int): The row to check.
        col (int): The column to check.

    Returns:
        bool: True if placing a queen at (row, col) is safe.
    """
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve(n, row, board, solutions):
    """Recursively search for solutions using backtracking.

    Args:
        n (int): The size of the board.
        row (int): The current row being filled.
        board (list): The current partial solution, board[r] = c.
        solutions (list): The list collecting all found solutions.
    """
    if row == n:
        solutions.append([[r, board[r]] for r in range(n)])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve(n, row + 1, board, solutions)
            board[row] = -1


def main():
    """Parse arguments and print all solutions to the N queens puzzle."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    board = [-1] * n
    solve(n, 0, board, solutions)

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
    