# 448. Find All Numbers Disappeared in an Array
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
 

# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
       
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - (abs(nums[index]))

        res = [i + 1 for i, num in enumerate(nums) if num > 0 ]
        return res

# This function works by iterating over the array and for each number nums[i], marking the number at the index abs(nums[i]) - 1 as negative. Then it returns a list of all indices i for which nums[i] is positive, adding 1 to each index to get the original number.

# For example, if the input is nums = [4,3,2,7,8,2,3,1], the output will be [5,6]. This is because 5 and 6 are the numbers in the range from 1 to n that do not appear in nums.

# This solution has a linear runtime complexity and uses constant extra space, as it modifies the input array in-place and does not use any additional data structures


# Initialization: The nums array is [4,3,2,7,8,2,3,1]. We don’t need to do anything for the first two numbers because their values are already provided.
# Iteration:
# For i=0 (the first number), we calculate index = abs(nums[i]) - 1 = 4 - 1 = 3. We then update nums[index] to be negative, so nums[3] becomes -7. Now, the nums array becomes [4,3,2,-7,8,2,3,1].
# We repeat this process for the remaining numbers. After iterating through all the numbers, the nums array becomes [-4,-3,-2,-7,8,2,-3,-1].
# Final step: We return a list of all indices i for which nums[i] is positive, adding 1 to each index to get the original number. So, the indices are 4 and 5, and adding 1 to each index gives us [5,6].
# So, the output is [5,6], which means the numbers 5 and 6 do not appear in nums.

# This is achieved by the property of the absolute function and the minus sign: for any number x, abs(x) gives the original number, and making a number negative does not change its absolute value but indicates that the number has been visited.