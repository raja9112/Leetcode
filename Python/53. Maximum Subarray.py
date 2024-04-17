class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        current = 0

        for n in nums:
            # Time: 519ms
            if current < 0:
                current = 0
            current += n
            max_sub = max(max_sub, current)
            
            # Time: 569ms
            # current = max(n, current+n)
            # max_sub = max(max_sub, current)
            
        return max_sub
        # We don't need negative number since the output is a largest number(positive number), 
        # so we are iterate throught the nums to increment the value of current, while iteration igf the current's is less than 0, make current = 0 and 
        # continue process and check which is the max number from max_sub or current and assign it to max_sub in every iteration and after looping, return the max_sub.
        
        
# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.