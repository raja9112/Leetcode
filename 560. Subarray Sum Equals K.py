# 560. Subarray Sum Equals K

# Medium

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0

        prefix = {0: 1}

        for n in nums:
            curSum += n
            diff = curSum - k

            res += prefix.get(diff, 0)
            prefix[curSum] = 1+ prefix.get(curSum, 0)

        return res

# let’s take the same input nums = [1, 1, 1] and k = 2 and see how it’s processed by the subarraySum function in detail:

# Initialize res to 0 and curSum to 0. These variables keep track of the total number of subarrays whose sum equals to k and the cumulative sum of the numbers as we iterate through nums, respectively.
# Initialize prefix to {0: 1}. This dictionary maps a sum to the number of subarrays that have that sum. The initial value {0: 1} means there’s one subarray (the empty subarray) with sum 0.
# Iterate over each number in nums. For each number, do the following:
# Add the number to curSum. For the first number in nums, curSum becomes 1.
# Calculate diff as curSum - k. For the first number, diff becomes -1.
# Increment res by the number of subarrays that have sum diff. Since there are no subarrays with sum -1, res remains 0.
# Increment the count of subarrays that have sum curSum in prefix. prefix becomes {0: 1, 1: 1}.
# Repeat the above step for the remaining numbers in nums. After processing the second number, curSum becomes 2, diff becomes 0, res becomes 1, and prefix becomes {0: 1, 1: 2}.
# After processing the third number, curSum becomes 3, diff becomes 1, res becomes 2, and prefix becomes {0: 1, 1: 2, 2: 1, 3: 1}.
# Return res as the total number of continuous subarrays whose sum equals to k. In this case, the function returns 2.
# So, for the input nums = [1, 1, 1] and k = 2, there are 2 subarrays whose sum equals to 2: [1, 1] from nums[0] to nums[1] and [1, 1] from nums[1] to nums[2].

# Here’s a more detailed step-by-step computation:

# Start with nums = [1, 1, 1] and k = 2.
# Initialize res = 0, curSum = 0, and prefix = {0: 1}.
# For the first number 1 in nums:
# curSum becomes 1.
# diff becomes -1.
# res remains 0 because there are no subarrays with sum -1.
# prefix becomes {0: 1, 1: 1}.
# For the second number 1 in nums:
# curSum becomes 2.
# diff becomes 0.
# res becomes 1 because there is one subarray with sum 0 (the empty subarray).
# prefix becomes {0: 1, 1: 2, 2: 1}.
# For the third number 1 in nums:
# curSum becomes 3.
# diff becomes 1.
# res becomes 2 because there are two subarrays with sum 1 ([1] from nums[0] to nums[0] and [1] from nums[1] to nums[1]).
# prefix becomes {0: 1, 1: 2, 2: 1, 3: 1}.
# Finally, return res, which is 2.