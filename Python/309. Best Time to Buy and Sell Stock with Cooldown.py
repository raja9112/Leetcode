# 309. Best Time to Buy and Sell Stock with Cooldown

# Medium

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

# Example 1:

# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# Example 2:

# Input: prices = [1]
# Output: 0
 

# Constraints:

# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0

            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i+1, buying)
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]
        return dfs(0, True)

# Iteration 1 (i = 0, buying = True): The current price is 1. cooldown becomes dfs(1, True) = 2 and buy becomes dfs(1, False) - 1 = 1. So, dp[(0, True)] becomes max(1, 2) = 2.
# Iteration 2 (i = 0, buying = False): The current price is 1. cooldown becomes dfs(1, False) = 1 and sell becomes dfs(2, True) + 1 = 3. So, dp[(0, False)] becomes max(3, 1) = 3.
# Iteration 3 (i = 1, buying = True): The current price is 2. cooldown becomes dfs(2, True) = 1 and buy becomes dfs(2, False) - 2 = -1. So, dp[(1, True)] becomes max(-1, 1) = 1.
# Iteration 4 (i = 1, buying = False): The current price is 2. cooldown becomes dfs(2, False) = 0 and sell becomes dfs(3, True) + 2 = 2. So, dp[(1, False)] becomes max(2, 0) = 2.
# Iteration 5 (i = 2, buying = True): The current price is 3. cooldown becomes dfs(3, True) = 0 and buy becomes dfs(3, False) - 3 = -3. So, dp[(2, True)] becomes max(-3, 0) = 0.
# Iteration 6 (i = 2, buying = False): The current price is 3. cooldown becomes dfs(3, False) = 0 and sell becomes dfs(4, True) + 3 = 3. So, dp[(2, False)] becomes max(3, 0) = 3.
# The remaining iterations follow the same pattern. At the end of the loop, dp[(0, True)] is 3, which is the maximum profit that can be achieved.
 
 
        # Method 2
        # n = len(prices)
        
        # hold, cool, sold = float('-inf'), 0, float('-inf')
        # for i in range(len(prices)):
        #     temp_sold = sold
        #     sold = prices[i] + hold
        #     hold = max(hold, cool - prices[i])
        #     cool = max(cool, temp_sold)
        
        # return max(sold, cool)