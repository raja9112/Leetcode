# 643. Maximum Average Subarray I

# EASY - Leetcode 75

# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000
 

# Constraints:

# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # Initialize currSum and maxSum to the sum of the initial k elements
        currSum = maxSum = sum(nums[:k])

        # Start the loop from the kth element 
        # Iterate until you reach the end
        for i in range(k, len(nums)):

            # Subtract the left element of the window
            # Add the right element of the window
            currSum += nums[i] - nums[i - k]
            
            # Update the max
            maxSum = max(maxSum, currSum)

        # Since the problem requires average, we return the average
        return maxSum / k

# Let's walk through the example nums = [1, 12, -5, -6, 50, 3] and k = 4.

# Initialization:

# Initial subarray of length k: [1, 12, -5, -6]
# currSum = 1 + 12 + (-5) + (-6) = 2
# maxSum = 2

# Sliding Window:

# Iteration 1 (i = 4):
# New element: 50
# Element leaving the window: 1
# Update currSum: currSum = currSum + nums[i] - nums[i - k]
# currSum = 2 + 50 - 1 = 51
# Update maxSum: maxSum = max(maxSum, currSum)
# maxSum = max(2, 51) = 51

# Iteration 2 (i = 5):
# New element: 3
# Element leaving the window: 12
# Update currSum: currSum = currSum + nums[i] - nums[i - k]
# currSum = 51 + 3 - 12 = 42
# Update maxSum: maxSum = max(maxSum, currSum)
# maxSum = max(51, 42) = 51

# Return the Maximum Average:
# maxSum = 51
# Average = maxSum / k = 51 / 4 = 12.75
# Thus, the maximum average subarray of length k is 12.75.