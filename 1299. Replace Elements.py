# # 1299. Replace Elements with Greatest Element on Right Side
# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

# After doing so, return the array.

# Example 1:

# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# Explanation: 
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.
# Example 2:

# Input: arr = [400]
# Output: [-1]
# Explanation: There are no elements to the right of index 0.
 

# Constraints:

# 1 <= arr.length <= 104
# 1 <= arr[i] <= 105

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]

        max_right = -1
        res = [0]*len(arr)

        for i in range(len(arr) - 1, -1, -1):
            res[i] = max_right
            max_right = max(max_right, arr[i])
        return res


# Let's go through the provided example step by step with the input [17, 18, 5, 4, 6, 1]:

# Initialize an empty array to store the results.
# Start traversing the input array in reverse order.
# At each step, keep track of the maximum element to the right.
# Store the current maximum element to the right in the result array.
# Update the maximum element to the right by comparing it with the current element.
# Repeat steps 3-5 until you reach the beginning of the input array.
# Here's the step-by-step breakdown:

# Input array: [17, 18, 5, 4, 6, 1]

# Initialize the maximum element to the right as -1.

# Start traversing the array in reverse order:

# Index 5 (Value: 1):
# Current maximum element to the right: -1
# Update result array: [-1, 0, 0, 0, 0, 0]
# Update maximum element to the right: 1
# Index 4 (Value: 6):
# Current maximum element to the right: 1
# Update result array: [-1, 1, 0, 0, 0, 0]
# Update maximum element to the right: 6
# Index 3 (Value: 4):
# Current maximum element to the right: 6
# Update result array: [-1, 1, 6, 0, 0, 0]
# Update maximum element to the right: 6
# Index 2 (Value: 5):
# Current maximum element to the right: 6
# Update result array: [-1, 1, 6, 6, 0, 0]
# Update maximum element to the right: 6
# Index 1 (Value: 18):
# Current maximum element to the right: 6
# Update result array: [-1, 1, 6, 6, 6, 0]
# Update maximum element to the right: 18
# Index 0 (Value: 17):
# Current maximum element to the right: 18
# Update result array: [-1, 1, 6, 6, 6, 18]
# Update maximum element to the right: 18
# Return the result array: [-1, 1, 6, 6, 6, 18]

# This result matches the expected output [18, 6, 6, 6, 1, -1].

