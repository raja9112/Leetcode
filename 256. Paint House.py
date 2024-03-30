class Solution:
    def minCost(self, costs: list[list[int]]):
        dp = [0, 0, 0]
        
        for i in range(len(costs)):
            dp0 = costs[i][0] + min(dp[1], dp[2])
            dp1 = costs[i][1] + min(dp[0], dp[2])
            dp2 = costs[i][2] + min(dp[0], dp[1])
            
            dp = [dp0, dp1, dp2]
            
        return min(dp)
        
obj = Solution()
print(obj.minCost([[17, 2, 17], [16, 16, 5], [14, 3, 19]]))  # 2 + 5 + 3 = 10


# This Python code is an implementation of a dynamic programming solution for a problem where you have to paint n houses with certain costs associated with painting each house with a certain color. 
# The problem’s constraint is that no two adjacent houses can have the same color.

# The minCost function takes a list of lists as input, where costs[i][j] represents the cost of painting the i-th house with the j-th color. It initializes a list dp with three zeros, representing the minimum cost of painting the houses up to the current house with each of the three colors.

# Then, for each house (from the first to the last), it calculates the cost of painting that house with each color, which is the cost of painting the house with that color plus the minimum cost of painting the previous houses with a different color. These costs are stored in dp0, dp1, and dp2.

# After calculating these costs, it updates dp with the new costs. This process is repeated for all the houses.

# Finally, it returns the minimum cost in dp, which represents the minimum cost of painting all the houses with the constraint that no two adjacent houses have the same color.

# In the example you provided, the function is called with costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]. 
# The output of the function is 10, which is the minimum cost of painting all the houses with the given costs and 
# the constraint that no two adjacent houses have the same color. 
# This is achieved by painting the first house with the second color (cost = 2), the second house with the third color (cost = 5), 
# and the third house with the second color (cost = 3), for a total cost of 2 + 5 + 3 = 10.