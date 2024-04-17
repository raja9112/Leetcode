# 79. Word Search

# Medium

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        path = set()
        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or 
                r >= row or c >= col or 
                word[i] != board[r][c] or 
                (r, c) in path):
                return False

            path.add((r, c))
            res =  (dfs(r+1, c, i+1) or
                dfs(r-1, c, i+1) or
                dfs(r, c+1, i+1) or
                dfs(r, c-1, i+1))

            path.remove((r, c))
            return res

        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
                
        return False

# Initialize row, col, and path: row and col are the dimensions of the board. path is a set used to keep track of the cells that have been visited.
# Define a helper function dfs: This function performs a depth-first search on the board. It takes three arguments: r and c are the current row and column, and i is the current character in the word.
# Base case of dfs: If i is equal to the length of the word, it means we have found the word on the board.
# Recursive case of dfs: If the current cell is valid (within the board boundaries, has not been visited before, and its value is equal to the current character in the word), it adds the cell to the path and recursively calls dfs for each of its neighbors. If the recursive call returns True, it also returns True. Otherwise, it removes the cell from the path and returns False.
# Iterate over the board: For each cell on the board, it calls dfs with the cell coordinates and the first character of the word. If dfs returns True, it returns True.
# Return False: If no valid word is found after checking all cells, it returns False.

# Time complexity: O(MN4^L)
# space complexity: O(L)

# M is the number of rows in the board,
# N is the number of columns in the board, and
# L is the length of the word.   