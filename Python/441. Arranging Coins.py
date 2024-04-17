# 441. Arranging Coins
# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

 

# Example 1:


# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.
# Example 2:


# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.
 

# Constraints:

# 1 <= n <= 231 - 1

class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        res = 0

        while l <= r:
            mid = (l + r) // 2
            cost = (mid/2)*(mid+1)          # Using formula to solve the problem

            if cost > n:
                r = mid -1
            else:
                l = mid + 1
                res = max(res, mid)
        return res

# let’s break down how the arrangeCoins function works with the input n = 5.

# Initialization: The input n is 5. We initialize l to 0, r to 5, and res to 0.
# Iteration:
# For the first iteration, we calculate mid = (l + r) // 2 = (0 + 5) // 2 = 2. We then calculate cost = (mid/2)*(mid+1) = (2/2)*(2+1) = 3.
# Since cost is not greater than n, we update l to mid + 1 = 2 + 1 = 3 and res to max(res, mid) = max(0, 2) = 2.
# For the second iteration, we calculate mid = (l + r) // 2 = (3 + 5) // 2 = 4. We then calculate cost = (mid/2)*(mid+1) = (4/2)*(4+1) = 10.
# Since cost is greater than n, we update r to mid - 1 = 4 - 1 = 3.
# For the third iteration, we calculate mid = (l + r) // 2 = (3 + 3) // 2 = 3. We then calculate cost = (mid/2)*(mid+1) = (3/2)*(3+1) = 6.
# Since cost is greater than n, we update r to mid - 1 = 3 - 1 = 2.
# The loop ends because l is not less than or equal to r.
# Final step: We return res, which is 2.
# So, the output is 2, which means the maximum number of complete rows that can be formed with 5 coins is 2.