# 36. Valid Sudoku

# Medium

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

# Example 1:


# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = collections.defaultdict(set)
        row = collections.defaultdict(set)
        square = collections.defaultdict(set)  # key = (r // 3, c // 3)

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue
                
                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in square[(r // 3, c // 3)]:
                    return False

                col[c].add(board[r][c])
                row[r].add(board[r][c])
                square[(r // 3, c // 3)].add(board[r][c])

        return True

# Here’s a breakdown of the code:

# isValidSudoku function: This function takes a 2D list board as input, which represents a Sudoku board, and returns a boolean indicating whether the board is valid.
# It initializes three dictionaries row, col, and square to keep track of the numbers present in each row, column, and 3x3 square, respectively.
# It then iterates over each cell in the board. If the cell is not empty (i.e., not “.”), it checks if the number in the cell is already present in the corresponding row, column, or 3x3 square. If it is, the board is not valid, so it returns False.
# If the number is not already present, it adds the number to the corresponding row, column, and 3x3 square.
# If it has checked all cells and hasn’t found any duplicates, the board is valid, so it returns True.
# This solution has a time complexity of O(1) because the size of the Sudoku board is fixed (9x9). The space complexity is also O(1) for the same reason.
