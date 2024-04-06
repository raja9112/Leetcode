# 1911. Maximum Alternating Subsequence Sum

# Medium

# The alternating sum of a 0-indexed array is defined as the sum of the elements at even indices minus the sum of the elements at odd indices.

# For example, the alternating sum of [4,2,5,3] is (4 + 5) - (2 + 3) = 4.
# Given an array nums, return the maximum alternating sum of any subsequence of nums (after reindexing the elements of the subsequence).

# A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order. For example, [2,7,4] is a subsequence of [4,2,3,7,2,1,4] (the underlined elements), while [2,4,2] is not.

 

# Example 1:

# Input: nums = [4,2,5,3]
# Output: 7
# Explanation: It is optimal to choose the subsequence [4,2,5] with alternating sum (4 + 5) - 2 = 7.
# Example 2:

# Input: nums = [5,6,7,8]
# Output: 8
# Explanation: It is optimal to choose the subsequence [8] with alternating sum 8.
# Example 3:

# Input: nums = [6,2,1,2,4,5]
# Output: 10
# Explanation: It is optimal to choose the subsequence [6,1,5] with alternating sum (6 + 5) - 1 = 10.
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # dp = {}

        # def dfs(i, even):
        #     if i == len(nums):
        #         return 0

        #     if (i, even) in dp:
        #         return dp[(i, even)]

        #     total = nums[i] if even else (-1 * nums[i])
        #     dp[(i, even)] = max(total + dfs(i+1, not even), dfs(i+1, even))
        #     return dp[(i, even)]


        # return dfs(0, True)

        sumEven = sumOdd = 0
        for i in range(len(nums)-1, -1, -1):
            sumEven = max(sumOdd + nums[i], sumEven)
            sumOdd = max(sumEven - nums[i], sumOdd)
        return sumEven

        # nums = [3, 2, 5, 10, 7]
        # Iteration 1 (i = 4): The current number is 7. sumEven becomes max(0 + 7, 0) = 7 and sumOdd remains 0.
        # Iteration 2 (i = 3): The current number is 10. sumEven becomes max(0 + 10, 7) = 10 and sumOdd becomes max(7 - 10, 0) = 0.
        # Iteration 3 (i = 2): The current number is 5. sumEven becomes max(0 + 5, 10) = 10 and sumOdd becomes max(10 - 5, 0) = 5.
        # Iteration 4 (i = 1): The current number is 2. sumEven becomes max(5 + 2, 10) = 10 and sumOdd becomes max(10 - 2, 5) = 8.
        # Iteration 5 (i = 0): The current number is 3. sumEven becomes max(8 + 3, 10) = 11 and sumOdd becomes max(10 - 3, 8) = 8.
        # At the end of the loop, sumEven is 11, which is the maximum sum of non-adjacent elements in the list.