# 73. Set Matrix Zeroes

# Medium

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

 

# Example 1:


# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Example 2:


# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

# Constraints:

# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1
 

# Follow up:

# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROW, COL = len(matrix), len(matrix[0])
        rowzero = False
        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r>0:
                        matrix[r][0] = 0
                    else:
                        rowzero = True

        for r in range(1, ROW):
            for c in range(1, COL):
                if matrix[0][c] == 0 or matrix[r][0]==0:
                    matrix[r][c]=0

        if matrix[0][0] == 0:
            for r in range(ROW):
                matrix[r][0] = 0

        if rowzero:
            for c in range(COL):
                matrix[0][c] = 0

# Here’s how the function would work with this input:

# Initialize variables: ROW and COL are the dimensions of the matrix. rowzero is a boolean variable used to check if the first row contains a zero.
# First pass: It iterates over each element in the matrix. If an element is zero, it sets the first element of its row and column to zero. If the zero element is in the first row, it sets rowzero to True.
# Second pass: It iterates over each element in the matrix, excluding the first row and column. If the first element of its row or column is zero, it sets the element to zero.
# Check the first column: If the first element of the matrix is zero, it means the first column should be set to zero. It iterates over the first column and sets each element to zero.
# Check the first row: If rowzero is True, it means the first row should be set to zero. It iterates over the first row and sets each element to zero.

# Time complexity: O(m+n)
# Spacer complexity: O(1)

# Method 2
# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         m, n = len(matrix), len(matrix[0])
#         zeroRows = [False]*m
#         zeroCols = [False]*n
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     zeroRows[i] = zeroCols[j] = True
#         for i in range(m):
#             for j in range(n):
#                 if zeroRows[i] or zeroCols[j]:
#                     matrix[i][j] = 0