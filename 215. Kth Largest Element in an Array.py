# 215. Kth Largest Element in an Array

# Medium

# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
 

# Constraints:

# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]

        # Quick Select algorithm - Time limit exceeds.
        # k = len(nums) - k

        # def quickselect(l, r):
        #     pivot, p = nums[r], l

        #     for i in range(l, r):
        #         if nums[i] <= pivot:
        #             nums[i], nums[p] = nums[p], nums[i]
        #             p += 1
        #     nums[p], nums[r] = nums[r], nums[p]

        #     if p > k: return quickselect(l, p-1)
        #     elif p < k: return quickselect(p+1, r)
        #     else: return nums[p]

        # return quickselect(0, len(nums)-1)
        
        