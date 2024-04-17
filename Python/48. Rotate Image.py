# 48. Rotate Image

# Medium

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:


# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # l, r = 0, len(matrix)-1

        # while l<r:
        #     for i in range(r-l):
        #         top, bottom = l, r
        #         # Storing top left value in tmp
        #         tmp = matrix[top][l+i]

        #         # Bottom left into top left
        #         matrix[top][l+i] = matrix[bottom-i][l]

        #         # Bottom right to bottom left
        #         matrix[bottom-i][l] = matrix[bottom][r-i]

        #         # Top right into bottom right
        #         matrix[bottom][r-i] = matrix[top+i][r]

        #         # top left into top right
        #         matrix[top+i][r] = tmp


        # Method 2
        # time complexity: O(n^2)
        n = len(matrix)

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i] = matrix[i][::-1]

# Transpose the matrix: The outer loop and the inner loop go through each element in the upper triangle of the matrix (where row index <= column index). For each element at (i, j), it swaps this element with the element at (j, i). After this step, the matrix is transposed, meaning its rows are turned into columns and vice versa.
# Reverse each row: The loop goes through each row in the matrix and reverses the order of elements in the row. This is done using Python’s slice notation with a step of -1, which produces a reversed copy of the list.
# Together, these two steps have the effect of rotating the matrix 90 degrees clockwise.

# Here’s an example to illustrate how it works:

# Suppose the input matrix is:

# 1 2 3
# 4 5 6
# 7 8 9

# After the transpose step, the matrix becomes:

# 1 4 7
# 2 5 8
# 3 6 9

# After the reverse step, the matrix becomes:

# 7 4 1
# 8 5 2
# 9 6 3