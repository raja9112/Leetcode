# 162. Find Peak Element

# Medium - Leetcode 75

# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

# Constraints:

# 1 <= nums.length <= 1000
# -231 <= nums[i] <= 231 - 1
# nums[i] != nums[i + 1] for all valid i.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left =0
        right = len(nums)-1
        while(left < right):
            mid = left +(right-left+1)//2 # Right biased mid as left = mid in else condition # prevent infinite loop
            if nums[mid] < nums[mid-1]: # False condition # Dec function # go left # Find Last False i.e the Last elem for which this condition will be False 
                right = mid - 1
            else: # decreasing so peak will be before mid or it can be mid
                left = mid
        return left