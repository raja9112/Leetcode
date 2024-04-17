# 152. Maximum Product Subarray

# Medium

# Given an integer array nums, find a 
# subarray
#  that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax, currMin = 1, 1

        for n in nums:
            if n < 0:
                currMax, currMin = currMin, currMax
            currMax = max(n, currMax * n)
            currMin = min(n, currMin * n)

            res = max(res, currMax)
        return res

# Here’s how the program works with this input:

# The maxProduct function is called with [-2, 3, -4] as the input.
# The function initializes res as the maximum number in nums (which is 3), and currMax and currMin as 1.
# It then starts a loop that iterates over each number in nums. For each number, it does the following:
# If n is less than 0, it swaps currMax and currMin. This is because a negative number reverses the order when multiplied.
# It updates currMax as the maximum of n and the product of currMax and n.
# It updates currMin as the minimum of n and the product of currMin and n.
# It updates res as the maximum of res and currMax.
# Finally, after checking all numbers, it returns res, which is the maximum product of a subarray in nums.
# Let’s see how this works with the list [-2, 3, -4]:

# The first number is -2. currMax and currMin become -2, and res remains 3.
# The next number is 3. Since 3 is positive, currMax becomes 3 (-2*3), currMin becomes -6 (-2*3), and res becomes 6.
# The next number is -4. Since -4 is negative, it swaps currMax and currMin first. Then currMax becomes 24 (6*-4), currMin becomes -12 (-4*3), and res becomes 24.
# So the function correctly finds that the maximum product of a subarray in the list [-2, 3, -4] is 24

# Time complexity: O(n)
# Space complexity: O(1)