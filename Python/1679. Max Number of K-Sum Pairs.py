# 1679. Max Number of K-Sum Pairs

# Medium - Leetcode 75

# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.

 

# Example 1:

# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
# Example 2:

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= 109

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        l = operation= 0
        r = len(nums)-1
        
        while l < r:
            if nums[l] + nums[r] == k:
                l += 1
                r -= 1
                operation += 1
            elif nums[l] + nums[r] < k:
                l += 1
            else: r -= 1
        

        return operation

# Method 2

        # res = 0
        # d = Counter(nums)

        # for i in nums:
        #     if (i in d and d[i] > 0):
        #         d[i] -= 1
        #         y = k - i

        #         if (y in d and d[y] > 0):
        #             d[y] -= 1
        #             res += 1
        #         else:
        #             d[i] += 1
        # return res
            
# Method3 
        # cache = defaultdict(int)
        # num_ops = 0
        # for i in nums:
        #     if cache[i] > 0:
        #         cache[i] -= 1
        #         num_ops += 1
        #         continue
        #     cache[k-i] += 1
        # return num_ops