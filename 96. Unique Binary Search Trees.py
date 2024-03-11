# 96. Unique Binary Search Trees

# Medium

# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

# Example 1:

# Input: n = 3
# Output: 5
# Example 2:

# Input: n = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 19

class Solution:
    def numTrees(self, n: int) -> int:
        # dp[4] = dp[0] * dp[3] +
        #         dp[1] * dp[2] + 
        #         dp[2] * dp[1] +
        #         dp[3] * dp[1]

        dp = [1] * (n+1)

        # dp[0] = 1
        # dp[1] = 1

        for node in range(2, n+1):
            total = 0
            for root in range(1, node+1):
                left = root -1
                right = node - root
                total += dp[left] * dp[right]
            dp[node] = total

        return dp[n]

# Here’s a brief explanation of the code:

# dp is a list of size n+1 that stores the number of unique BSTs for each number of nodes from 0 to n. It is initialized with 1 because there is one unique BST for 0 or 1 node.
# The outer loop iterates over the number of nodes from 2 to n.
# For each number of nodes node, it initializes a variable total to 0 to store the total number of unique BSTs.
# The inner loop iterates over the number of nodes from 1 to node. For each number of nodes root, it calculates the number of nodes on the left left and the right right of the root. It then adds the product of the number of unique BSTs for left and right to total.
# After the inner loop, it updates dp[node] to total.
# Finally, it returns dp[n], which is the number of unique BSTs that can be constructed with n distinct nodes.
# This solution has a time complexity of O(n^2) and a space complexity of O(n)

# Here’s how the function works with this input:

# Initialize dp = [1, 1, 1, 1] (of size n+1).
# Iterate over the number of nodes from 2 to 3.
# For node = 2, initialize total = 0.
# Iterate over the number of nodes from 1 to 2. For each root, calculate the number of nodes on the left left and the right right of the root. Add the product of dp[left] and dp[right] to total.
# After the inner loop, update dp[2] to total, which is 2. So, dp = [1, 1, 2, 1].
# Repeat steps 3-5 for node = 3. After these iterations, dp = [1, 1, 2, 5].
# Finally, return dp[3], which is 5. This is the number of unique BSTs that can be constructed with 3 distinct nodes.
# So, the function returns 5 for the input 3.