# 877. Stone Game
# Medium

# Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

# The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.

# Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.

# Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.

 

# Example 1:

# Input: piles = [5,3,4,5]
# Output: true
# Explanation: 
# Alice starts first, and can only take the first 5 or the last 5.
# Say she takes the first 5, so that the row becomes [3, 4, 5].
# If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
# If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
# This demonstrated that taking the first 5 was a winning move for Alice, so we return true.
# Example 2:

# Input: piles = [3,7,2,3]
# Output: true
 

# Constraints:

# 2 <= piles.length <= 500
# piles.length is even.
# 1 <= piles[i] <= 500
# sum(piles[i]) is odd.

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # dp = {}
        # def dfs(l, r):
        #     if l > r:
        #         return 0

        #     if (l, r) in dp:
        #         return dp[(l, r)]

        #     even = True if (r-1) %2 else False

        #     left = piles[l] if even else 0
        #     right = piles[r] if even else 0

        #     dp[(l,r)] = max(dfs(l+1, r) + left, dfs(l, r-1) + right)
        #     return dp[(l, r)]

        # return dfs(0, len(piles)-1)
# Here’s a step-by-step explanation of the code:

# dp: This is a dictionary that will store the maximum number of stones that the first player can get for each subproblem, where a subproblem is defined by a pair of indices (l, r) representing a subarray of the pile.
# dfs function: This is a helper function that uses depth-first search to find the maximum number of stones that the first player can get for a given subarray of the pile, defined by the indices l and r.
# If l is greater than r, it means there are no more stones left, so it returns 0.
# If the pair (l, r) is already in dp, it returns the stored value.
# It checks if the current turn is even or odd by checking if (r-1) % 2 is 0. If the turn is even, it means it’s the first player’s turn, otherwise it’s the second player’s turn.
# It calculates the number of stones that the first player will get if they take the leftmost or rightmost stone, depending on whose turn it is.
# It updates dp[(l, r)] with the maximum number of stones that the first player can get by taking either the leftmost or rightmost stone and making the optimal choice in the remaining turns.
# Finally, it returns dp[(l, r)].
# The main part of the code calls dfs on the entire array of the pile (from index 0 to len(piles)-1), and returns the resulting maximum number of stones that the first player can get.

        alice = 0 
        bob = 0
        deq = deque(piles)
        while deq:
            if deq[0] > deq[-1]:
                alice += deq.popleft()
                bob += deq.pop()
  
            else:
                alice += deq.pop()
                bob += deq.popleft()

        return alice > bob
    
    