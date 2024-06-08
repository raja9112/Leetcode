# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

# Easy - Leetcode 75

# Example 1:

# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
# Example 2:

# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.
 

# Constraints:

# 2 <= cost.length <= 1000


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # DP
        # Method 1
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-2:])


        # Method 2 - Iterating from reverse
        # cost.append(0)  #Highest staircase    [10, 15, 20, 0]

        # for i in range(len(cost)-3, -1, -1):     # len(cost) - 3 == 2nd element
        #     cost[i] += min(cost[i+1], cost[i+2])
        # return (min(cost[0], cost[1]))

#[1,100,1,1,1,100,1,1,100,1].

# Initialization: The cost array is [1,100,1,1,1,100,1,1,100,1]. We don’t need to do anything for the first two stairs because their costs are already provided.
# Iteration:
# For i=2 (the third stair), we calculate the total cost to reach this stair. The cost of the current stair is 1. The cost to reach the previous two stairs are 1 and 100 respectively. So, we add the minimum of these two costs to the current stair’s cost: 1 + min(1, 100) = 1 + 1 = 2. Now, the cost array becomes [1, 100, 2, 1, 1, 100, 1, 1, 100, 1].
# We repeat this process for the remaining stairs. After iterating through all the stairs, the cost array becomes [1, 100, 2, 3, 3, 103, 4, 5, 104, 6].
# Final step: We return the minimum cost between the last two stairs, which are 104 and 6. So, the minimum cost to reach the top is 6.