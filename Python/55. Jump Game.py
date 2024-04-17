# 55. Jump Game

# Medium

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False

# It starts from the end of the list and sets the goal as the last index.
# Then it iterates over the list in reverse order.
# For each element, it checks if the current index plus the value at that index is greater than or equal to the goal. If it is, it updates the goal to the current index.
# Finally, it checks if the goal is zero (i.e., the first index). If it is, it means we can reach the first index from the last index, so it returns True. Otherwise, it returns False.
# This solution works in O(n) time complexity, where n is the length of the input list. It doesn’t require any extra space, so the space complexity is O(1).