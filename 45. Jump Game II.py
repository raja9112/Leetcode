# 45. Jump Game II

# Medium

# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].

class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) -1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res

# In the first iteration of the while loop, l is initially 0, not 1. Here’s the corrected step-by-step breakdown:

# For nums = [2, 3, 1, 1, 4], res = l = r = 0 initially.
# In the first iteration of the while loop, farthest is updated to be 0 + nums[0] = 2, l is updated to be 0 + 1 = 1, r is updated to be 2, and res is incremented to 1.
# In the second iteration of the while loop, farthest is updated to be 1 + nums[1] = 4, l is updated to be 2 + 1 = 3, r is updated to be 4, and res is incremented to 2.
# Now, r is not less than len(nums) - 1, so the while loop ends and res = 2 is returned.
# So, the output of the function with nums = [2, 3, 1, 1, 4] is 2, because the minimum number of jumps to reach the end of the array is 2 (from index 0 to index 1, then from index 1 to index 4). 