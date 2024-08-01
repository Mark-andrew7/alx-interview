#!/usr/bin/python3
"""
Solving the N queens puzzle challenge
"""

import sys


def print_board(board):
    """Print the board configuration."""
    for row in board:
        print(' '.join(row))


def is_safe(board, row, col, N):
    """Check if a queen can be placed on board[row][col]."""
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True


def solve_n_queens_util(board, col, N):
    """Utilize backtracking to solve the N Queens problem."""
    if col >= N:
        print_board(board)
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 'Q'
            solve_n_queens_util(board, col + 1, N)
            board[i][col] = '.'


def solve_n_queens(N):
    """Solve the N Queens problem and print all solutions."""
    board = [['.' for _ in range(N)] for _ in range(N)]
    solve_n_queens_util(board, 0, N)


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_n_queens(N)


if __name__ == "__main__":
    main()
