# 322. Coin Change

# Medium

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0
 

# Constraints:

# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a-c >= 0:
                    dp[a] = min(dp[a], 1+dp[a-c])

        return dp[amount] if dp[amount] != amount+1 else -1

# Suppose we have coins = [1, 2, 5] and amount = 11.

# Here’s how the program works:

# The function initializes a list dp of size amount + 1, and sets each element to amount + 1. This list will store the minimum number of coins needed to make up each amount from 0 to amount. The reason we initialize it to amount + 1 is to handle the case where it’s impossible to make up the amount with the given coins.
# The function then sets dp[0] to 0, because the minimum number of coins needed to make up the amount 0 is 0.
# The function then starts two nested loops. The outer loop iterates over each amount from 1 to amount, and the inner loop iterates over each coin in coins.
# For each coin, if the coin is less than or equal to the current amount, it updates dp[a] to be the minimum of dp[a] and 1 + dp[a - c]. This is because if we can use the current coin to make up the current amount, the minimum number of coins needed is either the previous minimum number or 1 plus the minimum number of coins needed to make up the amount a - c.
# Finally, after filling up the dp list, the function returns dp[amount] if dp[amount] is not amount + 1, otherwise it returns -1. This is because if dp[amount] is still amount + 1, it means that it’s impossible to make up the amount with the given coins.
# So for the input coins = [1, 2, 5] and amount = 11, the function will return 3, because the minimum number of coins needed to make up the amount 11 is 3 (using three coins of 5, 5, and 1)