class Solution:
    def climbStairs(self, n: int) -> int:
        # Explanation with image is in leetcode hint.
        if n <= 3:      #
            return n    #
        n1, n2 = 2, 3       #1, 1

        for i in range(4, n+1):     # for i in range(n-1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2
        
        # Recursion
        # this recursive solution has exponential time complexity, resulting in a lot of redundant calculations.
        # if n == 0 or n == 1:
        #     return 1
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        # DP - Memoization - Time  complexity exceeded for input 44
        # memo ={}

        # if n<=3:
        #     return n
        
        # if n not in memo:
        #     memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

        # return memo[n]
        
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:

# 1 <= n <= 45