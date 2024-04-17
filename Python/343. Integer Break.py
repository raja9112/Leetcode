# 343. Integer Break

# Medium

# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

# Return the maximum product you can get.

 

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# Example 2:

# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
 

# Constraints:

# 2 <= n <= 58

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1:1}
        for num in range(2, n+1):
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                val = dp[i] * dp[num - i]
                dp[num] = max(dp[num], val)
        
        return dp[n]

# Here’s a step-by-step explanation of the code:

# dp: This is a dictionary that will store the maximum product for each integer from 1 to n. It’s initially populated with a base case: 1 (which corresponds to a product of 1).
# The main loop iterates over each integer num from 2 to n.
# It initializes dp[num] to 0 if num is equal to n, and to num otherwise. This is because if num is less than n, it can be a part of the product, so its value is used. But if num is equal to n, it must be broken down further, so its value is not used directly.
# It then iterates over each integer i from 1 to num-1, and calculates the product of dp[i] and dp[num - i]. This represents the maximum product that can be obtained by breaking num into i and num - i and multiplying the maximum products for these two numbers.
# It updates dp[num] with the maximum of its current value and the calculated product.
# Finally, it returns dp[n], which represents the maximum product that can be obtained by breaking n into at least two positive integers and multiplying them together.

# n = 10
# Iteration 1 (num = 2): dp[2] is initialized to 2. The inner loop calculates val = dp[1] * dp[1] = 1, and updates dp[2] to max(2, 1) = 2.
# Iteration 2 (num = 3): dp[3] is initialized to 3. The inner loop calculates val = dp[1] * dp[2] = 2, and updates dp[3] to max(3, 2) = 3.
# Iteration 3 (num = 4): dp[4] is initialized to 4. The inner loop calculates val = dp[1] * dp[3] = 3 and val = dp[2] * dp[2] = 4, and updates dp[4] to max(4, 3, 4) = 4.
# Iteration 4 (num = 5): dp[5] is initialized to 5. The inner loop calculates val = dp[1] * dp[4] = 4, val = dp[2] * dp[3] = 6, and updates dp[5] to max(5, 4, 6) = 6.
# The remaining iterations follow the same pattern. At the end of the loop, dp[10] is 36, 