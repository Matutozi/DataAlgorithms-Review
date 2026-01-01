"""
Leetcode 51

no two queens ever attack each other , no two queens can be in same row, column, diganonal
Using backtracking (brute force method)

keep track of column, row, diagnonals(-ve, +ve) that u place the queen, using a set()
along negative diagonal (row - column) = constant throught all cells in the diagonal
along positive diagonal (row + column) = constant

"""

def solveNQueen(n):
    column = set()
    pos_diag = set()
    neg_diag = set()

    result = list()
    board = [["."] * n for i in range(n)]

    def backtracking(r):
        if r == n:
            board_copy = ["".join(row) for row in board]
            result.append(board_copy)

            return 
        
        for c in range(n):
            if c in column or (r + c) in pos_diag or (r-c) in neg_diag:
                continue
            
            column.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r-c)
            board[r][c] = "Q"

        backtracking(r + 1)
        column.removq(c)
        pos_diag.remove(r + c)
        neg_diag.remove(r-c)
        board[r][c] = "."

    backtracking(0)
    return result