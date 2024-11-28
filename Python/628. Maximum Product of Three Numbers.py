# 628. Maximum Product of Three Numbers

# EASY

# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: 6
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 24
# Example 3:

# Input: nums = [-1,-2,-3]
# Output: -6
 

# Constraints:

# 3 <= nums.length <= 104
# -1000 <= nums[i] <= 1000


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        # Time: O(n)
        # Space: O(1)

        # We can use sort() but the time complexity will become O(n log n)

        if len(nums) < 3:
            return 0

        max1= max2= max3 = float("-inf")
        min1= min2 = float("inf")

        for num in nums:
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num

            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num

        return max(max1 * max2 * max3 , min1 * min2 * max1)