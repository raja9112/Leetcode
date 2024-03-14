# 62. Unique Paths

# Medium

# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

# Example 1:


# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
 

# Constraints:

# 1 <= m, n <= 100

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        for i in range(1, m+1):
            memo[(i, 1)] = 1
        for j in range(1, n + 1):
            memo[(1, j)] = 1

        for i in range(2, m+1):
            for j in range(2, n+1):
                memo[(i, j)] = memo[(i-1, j)] + memo[(i, j-1)]

        return memo[(m, n)]

# This is a Python solution for the problem of finding the number of unique paths in a grid. The problem is based on the idea that you start at the top-left corner of a m x n grid and you want to reach the bottom-right corner. You can only move either down or right at any point in time.
# The function uniquePaths takes two integers m and n as input, representing the number of rows and columns in the grid, respectively, and returns the total number of unique paths from the top-left to the bottom-right corner.
# The solution uses dynamic programming to solve the problem. It initializes a dictionary memo where the key is a tuple (i, j) representing a cell in the grid and the value is the number of unique paths to that cell.
# The function first initializes the number of paths to each cell in the first row and first column to be 1, because there is only one way to reach these cells (either all the way right or all the way down).
# Then, for each cell (i, j) in the grid (starting from cell (2, 2)), it calculates the number of unique paths to that cell by adding the number of paths to the cell above it (i-1, j) and the cell to its left (i, j-1). This is because a path to a cell can only come from the cell above it or the cell to its left.
# Finally, the function returns the number of unique paths to the bottom-right corner, which is memo[(m, n)]
# This solution has a time complexity of O(mn) and a space complexity of O(mn)
