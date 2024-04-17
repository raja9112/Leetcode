# 279. Perfect Squares

# Medium

# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

# Example 1:

# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
 

# Constraints:

# 1 <= n <= 104

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0

        for target in range(1, n+1):
            for s in range(1, target+1):
                square = s * s
                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target - square])

        return dp[n]
    
   
# Here’s how the code works:

# Initialize a list dp of size n+1 with all elements set to n. This list will be used to store the minimum number of squares for all numbers up to n. The reason for initializing with n is that in the worst case, a number can always be represented as a sum of n 1’s (since 1 is a perfect square), so n is the maximum possible number of squares.
# Set dp[0] to 0, because zero can be represented as a sum of zero perfect squares.
# For each target from 1 to n, and for each square number s from 1 to target, calculate the square of s and check if it’s less than or equal to target. If it is, update dp[target] to be the minimum of its current value and 1 + dp[target - square]. This represents the choice of using or not using the current square number s.
# Finally, return dp[n], which represents the minimum number of perfect squares that sum to n.
# This solution has a time complexity of O(n^2) and a space complexity of O(n), where n is the input number 

# let’s use n = 12 as an example input for the code. Here’s how the code works with this input:

# Initialize a list dp of size n+1 (which is 13 in this case) with all elements set to n (which is 12). So, dp = [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12].
# Set dp[0] to 0. Now, dp = [0, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12].
# For each target from 1 to n (which is 12), and for each square number s from 1 to target, calculate the square of s and check if it’s less than or equal to target. If it is, update dp[target] to be the minimum of its current value and 1 + dp[target - square]. For example, when target = 4, s can be 1 or 2. The square of 1 is 1 and the square of 2 is 4, both of which are less than or equal to target. So, dp[4] is updated to be the minimum of dp[4] (which is 12) and 1 + dp[4 - 1] (which is 1 + dp[3]) and 1 + dp[4 - 4] (which is 1 + dp[0]). The minimum of these values is 1, so dp[4] is updated to 1. This process is repeated for all values of target from 1 to n. After this step, dp = [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, 3].
# Finally, return dp[n], which is dp[12] = 3. This represents the minimum number of perfect squares that sum to n.
# So, the output of the function with n = 12 is 3, because 12 can be represented as the sum of three perfect squares (4 + 4 + 4).