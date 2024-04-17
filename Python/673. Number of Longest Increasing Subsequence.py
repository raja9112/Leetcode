# 673. Number of Longest Increasing Subsequence
# Medium

# Given an integer array nums, return the number of longest increasing subsequences.

# Notice that the sequence has to be strictly increasing.

 

# Example 1:

# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
# Example 2:

# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.
 

# Constraints:

# 1 <= nums.length <= 2000
# -106 <= nums[i] <= 106

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {}

        lenLTS = res = 0

        for i in range(len(nums)-1, -1, -1):
            maxlen, maxCnt = 1, 1
            for j in range(i+1, len(nums)):
                
                if nums[j] > nums[i]:
                    length, count = dp[j]
                    if length+1 > maxlen:
                        maxlen, maxCnt = length + 1, count
                    elif length+1 == maxlen:
                        maxCnt += count

            if maxlen > lenLTS:
                lenLTS, res = maxlen, maxCnt
            elif maxlen == lenLTS:
                res += maxCnt

            dp[i] = [maxlen, maxCnt]
        return res
    
    