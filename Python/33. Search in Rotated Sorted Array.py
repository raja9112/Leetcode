# 33. Search in Rotated Sorted Array

# Medium

# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1
 

# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            # Need to check extra conditions for unsorted array
            # Left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l+=1
                else:
                    r -= 1
            # Right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r-= 1
                else:
                    l+=1
        return -1

# Here’s how the program would work with this input:

# Initialize two pointers: l is set to 0 and r is set to 6 (the last index of nums).
# Start a while loop: The loop continues as long as l (0) is less than or equal to r (6), which means there are still elements to be checked.
# Find the middle element: In the first iteration of the loop, it calculates the middle index mid as (0 + 6) // 2 = 3. The middle element is nums[3] which is 7.
# Check if the target is found: The target (0) is not equal to the middle element (7), so it doesn’t return mid.
# Decide which half to search next: Since nums[l] (which is 4) is not less than or equal to nums[mid] (which is 7), it means the right half is sorted. The target (0) is not greater than nums[r] (2) and not less than nums[mid] (7), so it should look in the right half next. It sets l to mid + 1, which is 4.
# Repeat the process: The process is repeated with the updated l and r. In the next iteration, mid is (4 + 6) // 2 = 5, and nums[mid] is 1. Since the target is not equal to 1, it again checks which half to search next. This time, since nums[l] (0) is less than or equal to nums[mid] (1), it means the left half is sorted. But the target (0) is not greater than nums[mid] (1) and not less than nums[l] (0), so it should look in the left half next. It sets r to mid - 1, which is 4.
# Return the target index: Now l is equal to r (both are 4), and nums[4] is equal to the target (0), so it returns 4.
# Return -1 if the target is not found: If the while loop ends without finding the target, it returns -1, indicating that the target is not in the list. But in this case, it found the target at index 4.
# So, for this input, the search method would return 4, indicating that the target 0 is at index 4 in the list nums.