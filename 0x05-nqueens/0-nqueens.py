#!/usr/bin/python3
"""
Solving the N queens puzzle challenge
"""

import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col):
    """Utilize backtracking to place queens on the board"""
    if col >= len(board):
        print_solution(board)
        return True

    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1) or res
            board[i][col] = 0

    return res


def solve_nqueens(n):
    """Initialize the board and call the utility function"""
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_nqueens_util(board, 0):
        print("Solution does not exist")
        return False
    return True


def print_solution(board):
    """Print the solution in the required format"""
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


if __name__ == "__main__":
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

    solve_nqueens(N)
