#!/usr/bin/python3
"""N queens puzzle
"""
import sys


def isSafe(board, row, col):
    """Check if the position is safe for the queen"""
    for c in range(col):
        if board[c] is row or abs(board[c] - row) is abs(c - col):
            return False
    return True


def solveNQ(board, col):
    """Solve the N queen problem"""
    if col is len(board):
        print(str([[c, board[c]] for c in range(len(board))]))
        return
    for row in range(len(board)):
        if isSafe(board, row, col):
            board[col] = row
            solveNQ(board, col + 1)


if __name__ == "__main__":
    if len(sys.argv) is not 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [0 for col in range(N)]
    solveNQ(board, 0)

