# 300. Longest Increasing Subsequence

# Medium

# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence
# .

 

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104
 

# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
        return max(dp)

# Here’s how the program works with this input:

# The lengthOfLIS function is called with [10, 9, 2, 5, 3, 7, 101, 18] as the input.
# The function initializes a list dp of size 8 (the length of nums), and sets each element to 1. This list will store the length of the longest increasing subsequence that ends at each index.
# It then starts a loop that iterates over each index in nums from right to left. For each index i, it does the following:
# It starts another loop that iterates over each index j to the right of i. For each index j, it checks if nums[i] is less than nums[j]. If it is, it updates dp[i] to be the maximum of dp[i] and 1 + dp[j]. This is because if nums[i] is less than nums[j], we can extend the increasing subsequence that ends at j by nums[i].
# Finally, after filling up the dp list, the function returns the maximum value in dp, which is the length of the longest increasing subsequence in nums.
# Let’s see how this works with the list [10, 9, 2, 5, 3, 7, 101, 18]:

# For the index 7 (the last index), dp[7] is 1 because the longest increasing subsequence that ends at 18 is [18].
# For the index 6, dp[6] is 2 because the longest increasing subsequence that ends at 101 is [18, 101].
# The process continues for the rest of the indices. In the end, dp is [4, 3, 3, 3, 2, 3, 2, 1].
# The maximum value in dp is 4, which is the length of the longest increasing subsequence in the list [10, 9, 2, 5, 3, 7, 101, 18].
# So the function correctly finds that the length of the longest increasing subsequence in the list [10, 9, 2, 5, 3, 7, 101, 18] is 4