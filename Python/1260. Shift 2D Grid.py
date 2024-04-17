# 1260. Shift 2D Grid

# Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

# In one shift operation:

# Element at grid[i][j] moves to grid[i][j + 1].
# Element at grid[i][n - 1] moves to grid[i + 1][0].
# Element at grid[m - 1][n - 1] moves to grid[0][0].
# Return the 2D grid after applying shift operation k times.

 

# Example 1:


# Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# Output: [[9,1,2],[3,4,5],[6,7,8]]
# Example 2:


# Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
# Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
# Example 3:

# Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
# Output: [[1,2,3],[4,5,6],[7,8,9]]
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m <= 50
# 1 <= n <= 50
# -1000 <= grid[i][j] <= 1000
# 0 <= k <= 100

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(grid), len(grid[0]) # getting the length of single row and lenght of single column, so we get to know how many row and cols are there by taking the lenght.

        def posToval(r, c):
            return r * N + c
        def valTopos(v):
            return [v//N, v%N] #r, c
        
        new = [[0]* N for i in range(M)]

        for r in range(M):
            for c in range(N):
                newval = (posToval(r, c) + k) % (M*N)
                newR, newC = valTopos(newval)
                new[newR][newC] = grid[r][c]

        return new

# Here’s how it works:

# The function shiftGrid takes a 2D list grid and an integer k as input.
# It initializes M and N to the number of rows and columns in grid.
# It defines two helper functions: posToval, which converts a position (r, c) in the grid to a value, and valTopos, which converts a value back to a position in the grid.
# It creates a new 2D list new with the same dimensions as grid, initialized with zeros.
# It then iterates over each cell in grid. For each cell, it calculates a new value newval by adding k to the value of the current cell and taking the remainder by M*N. This effectively shifts the cell k positions to the right, wrapping around to the start of the grid if necessary.
# It converts newval back to a position in the grid, and updates the corresponding cell in new to the value of the current cell in grid.
# Finally, it returns new, which is the grid after shifting.
# This solution has a time complexity of O(MN) because it needs to iterate over each cell in the grid, and it uses O(MN) extra space to store the new grid.

# Implemetation

# let’s break down how the shiftGrid function works with the input grid = [[1,2,3],[4,5,6],[7,8,9]] and k = 1.

# Initialization: The input grid is [[1,2,3],[4,5,6],[7,8,9]] and k is 1. We initialize M to 3 and N to 3 (the number of rows and columns in grid), and new to a 3x3 grid filled with zeros.
# Iteration:
# For r=0 (the first row) and c=0 (the first column), we calculate newval = (posToval(0, 0) + 1) % (3*3) = (0 + 1) % 9 = 1. We then calculate newR, newC = valTopos(1) = [0, 1]. We update new[0][1] to grid[0][0] = 1. Now, new becomes [[0, 1, 0], [0, 0, 0], [0, 0, 0]].
# We repeat this process for the remaining cells in grid. After iterating through all the cells, new becomes [[9, 1, 2], [3, 4, 5], [6, 7, 8]].
# Final step: We return new, which is [[9, 1, 2], [3, 4, 5], [6, 7, 8]].