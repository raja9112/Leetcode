# 34. Find First and Last Position of Element in Sorted Array

# Medium

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.search(nums, target, True)
        right = self. search(nums, target, False)
        return [left, right]


    def search(self, nums, target, leftbias):    
        l, r = 0, len(nums) -1 
        i = -1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                i = mid
                if leftbias:
                    r = mid - 1
                else:
                    l = mid + 1
        return i

# Here's a step-by-step explanation of how the code works:

# The searchRange method takes a sorted list of integers nums and a target integer target as input and returns a list containing the leftmost and rightmost indices of the target value in the list.

# Inside searchRange, it calls the search method twice:

# First, it calls search with leftbias set to True, indicating that it's searching for the leftmost occurrence of the target.
# Then, it calls search with leftbias set to False, indicating that it's searching for the rightmost occurrence of the target.
# The search method performs a binary search on the input list nums to find the target value target. The leftbias parameter determines whether the search should prioritize finding the leftmost occurrence (True) or the rightmost occurrence (False).

# Inside the search method:

# It initializes variables l and r to represent the left and right ends of the search range.
# It initializes variable i to store the index of the target value. If the target is not found, i remains -1.
# It enters a while loop that continues as long as l is less than or equal to r.
# In each iteration, it calculates the midpoint mid of the search range.
# If the value at the midpoint nums[mid] is greater than the target, it updates r to mid - 1 to search the left half of the range.
# If the value at the midpoint nums[mid] is less than the target, it updates l to mid + 1 to search the right half of the range.
# If the value at the midpoint nums[mid] is equal to the target, it updates i to mid, indicating that the target is found.
# If leftbias is True, it updates r to mid - 1 to continue searching for the leftmost occurrence of the target.
# If leftbias is False, it updates l to mid + 1 to continue searching for the rightmost occurrence of the target.
# Finally, it returns the index i, which contains the index of either the leftmost or the rightmost occurrence of the target value in the list.

# The searchRange method then returns a list containing the leftmost and rightmost indices of the target value, obtained from the two calls to the search method.

# This algorithm efficiently finds the leftmost and rightmost occurrences of the target value using binary search, resulting in a time complexity of O(log n), where n is the number of elements in the input list nums.