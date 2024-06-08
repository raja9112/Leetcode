# 216. Combination Sum III

# Medium - Leetcode 75

# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

# Example 1:

# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Explanation:
# 1 + 2 + 4 = 7
# There are no other valid combinations.
# Example 2:

# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations.
# Example 3:

# Input: k = 4, n = 1
# Output: []
# Explanation: There are no valid combinations.
# Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
 

# Constraints:

# 2 <= k <= 9
# 1 <= n <= 60


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(start, summ, curr):
            if len(curr) == k and summ == 0:
                res.append(curr[:])
            if len(curr) > k or summ < 0:
                return

            for i in range(start, 10):
                curr.append(i)
                backtrack(i + 1, summ - i, curr)
                curr.pop()


        backtrack(1, n, [])
        return res
    
    
# Initialization: Start with an empty result list and call the backtrack function with the initial parameters.

# Backtrack Function:
# Base Case: If the combination's length equals k and the remaining sum is zero, a valid combination is found.

# Pruning: If the combination's length exceeds k or the remaining sum becomes negative, stop exploring that path.

# Loop: Iterate through the numbers from the current start number to 9, add the current number to the combination, and recursively call the backtrack function with updated parameters. Remove the last number to backtrack and explore other combinations.

# Complexity
# Time complexity: O(9/k)
# Space complexity: O(k)