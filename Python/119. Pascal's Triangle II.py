# 119. Pascal's Triangle II

# EASY

# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]
 

# Constraints:

# 0 <= rowIndex <= 33
 

# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1] * (rowIndex + 1)

        for i in range(1, rowIndex + 1):
            for j in range(i-1, 0, -1):
                res[j] += res[j-1]

        return res

"""Loop through Rows
Outer Loop: We iterate over i from 1 to rowIndex. For each i, we will calculate the i-th row of Pascal's Triangle.

Iteration 1: i = 1
Current Row: [1, 1, 1, 1, 1]
Inner Loop: Loop j from 0 to 0 (i.e., 1 - 1 to 0), but since j will not enter the loop, nothing happens.
Result after this iteration: Row is still [1, 1, 1, 1, 1].

Iteration 2: i = 2
Current Row: [1, 1, 1, 1, 1]
Inner Loop: Loop j from 1 to 1 (i.e., 2 - 1 to 0).

First (and only) iteration of inner loop (j = 1):
Update: row[1] += row[0]
Calculation: row[1] = 1 + 1 = 2
Updated Row: [1, 2, 1, 1, 1]
Result after this iteration: Row is [1, 2, 1, 1, 1].

Iteration 3: i = 3
Current Row: [1, 2, 1, 1, 1]
Inner Loop: Loop j from 2 to 1 (i.e., 3 - 1 to 0).

First iteration of inner loop (j = 2):
Update: row[2] += row[1]
Calculation: row[2] = 1 + 2 = 3
Updated Row: [1, 2, 3, 1, 1]

Second iteration of inner loop (j = 1):
Update: row[1] += row[0]
Calculation: row[1] = 2 + 1 = 3
Updated Row: [1, 3, 3, 1, 1]
Result after this iteration: Row is [1, 3, 3, 1, 1].

Iteration 4: i = 4
Current Row: [1, 3, 3, 1, 1]
Inner Loop: Loop j from 3 to 1 (i.e., 4 - 1 to 0).

First iteration of inner loop (j = 3):
Update: row[3] += row[2]
Calculation: row[3] = 1 + 3 = 4
Updated Row: [1, 3, 3, 4, 1]

Second iteration of inner loop (j = 2):
Update: row[2] += row[1]
Calculation: row[2] = 3 + 3 = 6
Updated Row: [1, 3, 6, 4, 1]

Third iteration of inner loop (j = 1):
Update: row[1] += row[0]
Calculation: row[1] = 3 + 1 = 4
Updated Row: [1, 4, 6, 4, 1]

Final Result after this iteration: Row is [1, 4, 6, 4, 1]."""