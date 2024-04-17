# 136. Single Number
# Solved
# Easy
# Topics
# Companies
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        res = 0
        for i in nums:
            res = i ^ res
        return res

# The provided Python solution for the problem of finding the single number in a list where every other number appears twice does indeed satisfy these constraints. It uses the XOR operation to solve the problem with a linear runtime complexity and constant extra space.

# Here’s how it works:

# The function singleNumber takes a list of integers nums as input, where every integer appears twice except for one.
# It initializes a variable res to 0. This variable will eventually hold the single number that doesn’t appear twice.
# The function then iterates over each number i in nums. For each i, it updates res to be the result of i XOR res. The XOR operation is denoted by the ^ symbol.
# Since XOR of all numbers appearing twice will be zero and XOR of a number with zero is the number itself, res will be the number that appears only once in the array.
# Finally, it returns res, which is the single number that doesn’t appear twice in nums.
# This solution has a linear runtime complexity because it iterates over nums once, and it uses constant extra space because it only uses a fixed amount of space to store res, regardless of the size of nums.


# Initialization: The nums array is [4,1,2,1,2]. We initialize res to 0.
# Iteration:
# For the first number 4, we calculate res = 4 XOR 0 = 4.
# For the second number 1, we calculate res = 1 XOR 4 = 5.
# For the third number 2, we calculate res = 2 XOR 5 = 7.
# For the fourth number 1, we calculate res = 1 XOR 7 = 6.
# For the fifth number 2, we calculate res = 2 XOR 6 = 4.
# Final step: We return res, which is 4.
# So, the output is 4, which means the single number that doesn’t appear twice in nums is 4.

# This is achieved by the property of the XOR operation: for any number x, x XOR x = 0 and x XOR 0 = x. 
# So, all the numbers appearing twice in nums will XOR to 0, and the single number will be left.