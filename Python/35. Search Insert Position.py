class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return  
        # if target in nums:
        #     output=nums.index(target)
        #     return output
        # else:
        #     nums.append(target)
        #     nums.sort()
        #     output=nums.index(target)
        #     return output

        # for i, num in enumerate(nums):
        #     if num >= target:
        #         return i
        # return len(nums)


        # Binary search
        l = 0
        r = len(nums) - 1

        while l<=r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        n = len(nums) - 1
        nums.append(None)
        while n > l:
            nums[n] = nums[n-1]
            n -= 1
        nums[l] = target
        return l
        
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104