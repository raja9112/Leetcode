# 213. House Robber II

# Medium

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

# Example 1:

# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
# Example 2:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 3:

# Input: nums = [1,2,3]
# Output: 3
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(rob1+n, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

# The rob method takes a list of integers nums as input, where each integer represents the amount of money in a house. The function returns the maximum amount of money you can rob without robbing two adjacent houses.

# The helper method is a helper function that calculates the maximum amount of money you can rob from a linear street of houses.

# Here’s a brief explanation of the code:

# The rob function first checks if the list nums is empty. If it is, it returns 0. If it’s not, it returns the maximum of three values: the amount of money in the first house, the maximum amount of money you can rob from the second house to the last house, and the maximum amount of money you can rob from the first house to the second-to-last house. This is because you can’t rob both the first and last houses as they are adjacent in a circular street.
# The helper function takes a list of integers nums as input and returns the maximum amount of money you can rob from a linear street of houses. It initializes two variables rob1 and rob2 to 0. rob1 represents the maximum amount of money you can rob up to the previous house, and rob2 represents the maximum amount of money you can rob up to the current house.
# The helper function then iterates over the list nums. For each integer n, it calculates the maximum of rob1 + n and rob2, and assigns the result to a temporary variable temp. It then updates rob1 to rob2 and rob2 to temp.
# Finally, the helper function returns rob2, which is the maximum amount of money you can rob from the list nums.
# This solution has a time complexity of O(n) and a space complexity of O(1)
