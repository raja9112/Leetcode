# 334. Increasing Triplet Subsequence

# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# Example 3:

# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

# Constraints:

# 1 <= nums.length <= 5 * 105
# -231 <= nums[i] <= 231 - 1
 

# Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        first = second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False

# Space complexity: O(1)
# Time complexity: O(n)

# We keep 2 numbers first and second where first < second, and first number must be before second number.
# Iterate num in nums:
# If num <= first then update the first as minimum as possible, byfirst = num
# Else If num <= second then update second as minimum as possible (since now first < num <= second), by second = num
# Else, now first < second < num then we found a valid Increasing Triplet Subsequence, return True.
# Otherwise, return False.


# Method 2: Build Max Right So Far and Max Left So Far
            # n = len(nums)

            # maxRight = [0] * n
            # maxRight[-1] = nums[-1]

            # for i in range(n-2, -1, -1):
            #     maxRight[i] = max(maxRight[i+1], nums[i+1])
            
            # minLeft = nums[0]
            # for i in range(1, n-1):
            #     if minLeft < nums[i] < maxRight[i]:
            #         return True
            #     minLeft = min(minLeft, nums[i]) 
            # return False

# Method 3:
            # num_count = len(nums)
            # first_num = sys.maxsize
            # second_num = sys.maxsize
            # third_num = sys.maxsize
            
            # for i in range(num_count):
                
            #     if nums[i] < first_num:
            #         first_num = nums[i]
            #     elif nums[i] > first_num and nums[i] <= second_num:
            #         second_num = nums[i]
            #     elif nums[i] > first_num and nums[i] > second_num and nums[i] <= third_num:
            #         print([first_num, second_num, nums[i]])            
            #         return True
        
            # return False