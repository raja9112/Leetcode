# 78. Subsets

# Medium

# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):

            if i >= len(nums):
                res.append(subset.copy())
                return

            # Decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            # Decision to NOT incluse nums[i]
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res

# Here’s how the program would work with this input:

# Initialize a result list and a subset list: The res list is used to store the final results. The subset list is used to store the current subset.
# Define a helper function dfs: This function performs a depth-first search on the nums list. It takes one argument: i is the current index in nums.
# Base case of dfs: If i is equal to the length of nums, it means we have explored all elements in nums. It adds a copy of subset to res and returns.
# Recursive case of dfs: If i is less than the length of nums, it makes two decisions: include nums[i] in subset or not. For each decision, it recursively calls dfs with i+1.
# Start the depth-first search process: It calls dfs with 0 to start the depth-first search process.
# Return the result: Finally, it returns res, which contains all possible subsets of nums.