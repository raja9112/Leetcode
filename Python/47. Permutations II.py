# 47. Permutations II

# Medium

# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

# Example 1:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

# Constraints:

# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []

        count = {n:0 for n in nums}
        for n in nums:
            count[n] += 1

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for i in count:
                if count[i] > 0:
                    perm.append(i)
                    count[i] -= 1

                    dfs()

                    count[i] += 1
                    perm.pop()

        dfs()
        return res

# Here’s how it works:

# Initialize a result list, a permutation list, and a count dictionary: The res list is used to store the final results. The perm list is used to store the current permutation. The count dictionary is used to count the occurrences of each number in nums.
# Define a helper function dfs: This function performs a depth-first search on the nums list. It doesn’t take any arguments.
# Base case of dfs: If the length of perm is equal to the length of nums, it means we have formed a valid permutation. It adds a copy of perm to res and returns.
# Recursive case of dfs: If the length of perm is less than the length of nums, it iterates over each number in count. If the count of a number is greater than 0, it adds the number to perm, decrements its count, and recursively calls dfs. After the recursive call, it increments the count of the number and removes it from perm.
# Start the depth-first search process: It calls dfs to start the depth-first search process.
# Return the result: Finally, it returns res, which contains all unique permutations of nums.

# Time complexity: O(N*N!)
# Space complexity: O(N)

