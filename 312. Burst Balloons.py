# 312. Burst Balloons

# Hard

# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

# Return the maximum coins you can collect by bursting the balloons wisely.

 

# Example 1:

# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
# Example 2:

# Input: nums = [1,5]
# Output: 10
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# 0 <= nums[i] <= 100


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Brute force - write like a decision tree, from every node, You can start with poping 1 ballon either 3 or 1 or 5 or 8 in [3,1,5,8]
        # In the next iteration you have n-1 decisions to pop next array after pop
        # so time complexity - O(n^n)

        # Optimal approach
        # Time - O(n^3) - for every element we are going to iterate and find all the subarrays(O(n^2)), we have to iterate for every single value of a subarray

        # Add dummy balloons with value 1 at the beginning and end of the `nums` array
        nums = [1] + nums + [1]
        # Initialize a memoization dictionary to store computed results
        memory = {}

        # Define a recursive function `dfs` to compute maximum coins within a range [l, r]
        def dfs(l, r):
            # Base case: If l > r, return 0 - Nothing left to pop
            if l > r:
                return 0

            # If the result for the range [l, r] is memoized, return it
            if (l, r) in memory:
                return memory[(l, r)]
            
            # Initialize maximum coins within the range [l, r]
            memory[(l, r)] = 0
            # If we pop a ballon at index i last - Find out max number of coins we are going to get for this pair
            # Iterate over all possible choices of bursting balloons within the range [l, r]
            for i in range(l, r + 1):
                # if this was poped last the below is the number of coins you'd get
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                # 1. Number of coins you'll get from left subarray excluding i and right
                # 2. Number of coins you'll get from right subarray excluding i and left
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                # Update maximum coins for the current range [l, r]
                memory[(l, r)] = max(memory[(l, r)], coins)
            
            return memory[(l, r)]
        
        # Call the dfs function with the initial range [1, len(nums) - 2], to ignore [1] in left and right
        return dfs(1, len(nums) - 2)