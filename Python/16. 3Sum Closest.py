# 16. 3Sum Closest

# Medium

# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

# Constraints:

# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:  # To handle duplicate values if we don't want to use
                continue

            j = i + 1
            k = len(nums)-1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if abs(total - target) < abs(res - target):
                    res = total

                if total < target:
                    j += 1
                else:
                    k -= 1

        return res