# 416. Partition Equal Subset Sum

# Medium

# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
 

# Constraints:

# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums)-1, -1, -1):
            nextDP = set()
            for t in dp:
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP

        return False if target not in dp else True
    
    
    
# Algorithm:
# Check Sum Divisibility by 2:

# First, we check if the sum of all elements in the array is divisible by 2. If it's not, then it's impossible to partition the array into two subsets with equal sums, so we return False.
# Dynamic Programming (DP):

# We initialize a set dp to store all possible sums that can be achieved using elements of the array.
# We add 0 to dp to represent an empty subset (where the sum is 0).
# We calculate the target sum, which is half of the total sum of elements in the array, as we're trying to partition the array into two subsets with equal sums.
# We iterate through the elements of the array in reverse order (from the last element to the first).
# For each element nums[i], we create a new set nextDP to store the next set of possible sums.
# For each sum t in the current set dp, we add t + nums[i] (sum including nums[i]) and t (sum excluding nums[i]) to the nextDP.
# After processing all elements, we update dp to nextDP.
# Check Target Sum Existence:

# Finally, we check if the target sum (half of the total sum) exists in the dp set. If it does, it means it's possible to partition the array into two subsets with equal sums, so we return True; otherwise, we return False.
# Computational Part:
# The computational part involves iterating through each element of the array once and updating the set of possible sums. This step has a time complexity of O(n * sum(nums)), where 'n' is the number of elements in the array and 'sum(nums)' is the total sum of elements in the array.
# Checking whether the target sum exists in the set has an average time complexity of O(1) due to set lookup.
# Overall, the algorithm has a time complexity of O(n * sum(nums)).
# Example:
# Let's say nums = [1, 5, 11, 5].

# Total sum is 22.
# Target sum is 11.
# The set dp will be: {0, 1, 5, 6, 11, 12, 16, 17, 22}.
# As 11 exists in the set, we can partition the array into two subsets with equal sums.


# Iteration 1: i = 3, nums[i] = 5
# Current set dp: {0}
# Next set nextDP: {0, 5}

# Iteration 2: i = 2, nums[i] = 11
# Current set dp: {0, 5}
# Next set nextDP: {0, 5, 11, 16}

# Iteration 3: i = 1, nums[i] = 5
# Current set dp: {0, 5, 11, 16}
# Next set nextDP: {0, 5, 10, 11, 15, 16, 21, 22}

# Iteration 4: i = 0, nums[i] = 1
# Current set dp: {0, 5, 10, 11, 15, 16, 21, 22}
# Next set nextDP: {0, 1, 5, 6, 10, 11, 15, 16, 21, 22}
