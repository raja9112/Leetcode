# 221. Maximal Square

# Medium

# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

# Example 1:


# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
# Example 2:


# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
# Example 3:

# Input: matrix = [["0"]]
# Output: 0
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        # Dynamic programming: Bottom up approach
        # Recursive: Top - Bottom approach

        row, col = len(matrix), len(matrix[0])
        cache = {}      # map each (r, c) = MaxLenght of square

        def helper(r, c):
            if r >= row or c >= col:
                return 0

            if (r, c) not in cache:
                right = helper(r, c+1) # Adjancent column
                down = helper(r+1, c)  # Number in next row
                diag = helper(r+1, c+1) # To check diagonal number

                cache[(r, c)] = 0

                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(right, down, diag)

            return cache[(r, c)]

        helper(0, 0)
        return max(cache.values()) ** 2

# This is a Python solution for the problem of finding the largest square containing only 1’s in a 2D binary matrix. It uses a dynamic programming approach to solve the problem.

# The function maximalSquare takes a 2D matrix as input and returns the area of the largest square in the matrix that contains only 1’s.

# The helper function helper(r, c) is a recursive function that checks the value at the current cell (r, c). If the value is “1”, it calculates the size of the square by adding 1 to the minimum of the squares to the right, down, and diagonally down-right of the current cell. This is because a square can only be formed if all three neighboring squares are also squares of 1’s.

# The function uses memoization to store the size of the largest square at each cell in a cache, which significantly improves the efficiency of the function by avoiding redundant computations.

# Finally, the function returns the square of the maximum value in the cache, which represents the area of the largest square of 1’s in the matrix.

# This solution has a time complexity of O(mn) where m and n are the number of rows and columns in the matrix, respectively. The space complexity is also O(mn) due to the additional space required for the cache.