# 46. Permutations

# Medium 

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]
 

# Constraints:

# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1:  # Return the list if the lenght of list is 1
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)                 
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)

            res.extend(perms)
            nums.append(n)
        return res

# Here’s how the program works with this input:

# The permute function is called with [1, 2, 3] as the input.
# The function checks if the length of nums is 1. Since it’s not, it skips to the loop.
# In the first iteration of the loop, i is 0. It removes the first number from nums (which is 1) and stores it in n. Now nums is [2, 3] and n is 1.
# It then recursively calls permute on [2, 3]. This recursive call will return all permutations of [2, 3], which are [[2, 3], [3, 2]].
# For each of these permutations, it appends n (which is 1) to the end of the permutation. So the permutations become [[2, 3, 1], [3, 2, 1]].
# It adds these permutations to res and then appends n back to nums to restore it for the next iteration. Now res is [[2, 3, 1], [3, 2, 1]] and nums is [2, 3, 1].
# The process continues for the rest of the numbers in nums. After checking all numbers, res will contain all permutations of [1, 2, 3].
# Finally, it returns res, which is [[2, 3, 1], [3, 2, 1], [1, 3, 2], [3, 1, 2], [1, 2, 3], [2, 1, 3]].
# This means that the function correctly generated all permutations of the input list [1, 2, 3]. 


# The time complexity of this program is O(N*N!). Here’s why:

# There are N! (N factorial) permutations of a list of length N. This is because there are N choices for the first element, N-1 choices for the second element, and so on, down to 1 choice for the last element.
# For each permutation, the program makes a copy of the list when it calls nums[:]. This operation takes O(N) time.
# Therefore, the total time complexity is O(N*N!) because for each of the N! permutations, it does O(N) work.
# The space complexity of this program is O(N). Here’s why:

# There are at most N recursive calls on the call stack at any time, and each call has a constant amount of space overhead.
# The program also uses space to store the output. In the worst case, if all permutations are stored in the output list, it will take O(N!) space. However, this space is not counted towards the space complexity as it is necessary to store the output.
# So, the space complexity is O(N) due to the recursive call stack.

# Method 2 - Runtime: 66ms
def backtrack(nums, path): 
            if not nums: 
                result.append(path) 
                return 
            for i in range(len(nums)): 
                backtrack(nums[:i] + nums[i+1:], path + [nums[i]]) 
result = [] 
backtrack(nums, []) 
return result 