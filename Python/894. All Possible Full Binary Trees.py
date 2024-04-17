# 894. All Possible Full Binary Trees

# Medium

# Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

# Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

# A full binary tree is a binary tree where each node has exactly 0 or 2 children.

 

# Example 1:


# Input: n = 7
# Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# Example 2:

# Input: n = 3
# Output: [[0,0,0]]
 

# Constraints:

# 1 <= n <= 20

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {0: [], 1:[TreeNode()]}

        def dfs(n):
            if n in dp:
                return dp[n]

            res = []
            for l in range(n):
                r = n-1-l

                leftTree, rightTree = dfs(l), dfs(r)

                for t1 in leftTree:
                    for t2 in rightTree:
                        res.append(TreeNode(0, t1, t2))
            dp[n] = res
            return res

        return dfs(n)
    
# Here’s a step-by-step explanation of the code:

# TreeNode: This is a class for a binary tree node. Each node has a value val, a left child left, and a right child right.
# dp: This is a dictionary that will store all possible full binary trees for each number of nodes. It’s initially populated with two base cases: 0 nodes (which corresponds to an empty list of trees) and 1 node (which corresponds to a list containing a single tree with one node).
# dfs function: This is a helper function that uses depth-first search to find all possible full binary trees with a given number of nodes n.
# If n is already in dp, it returns the stored list of trees.
# It initializes an empty list res to store the result.
# It then iterates over each number l from 0 to n-1, and sets r to n-1-l. This represents all possible pairs of numbers of nodes in the left and right subtrees of a tree with n nodes.
# For each pair of numbers l and r, it gets the lists of all possible full binary trees with l and r nodes, respectively.
# It then iterates over each pair of trees t1 and t2 from the left and right lists of trees, respectively, and appends a new tree with t1 as the left child and t2 as the right child to res.
# Finally, it stores res in dp[n] and returns res.
# The allPossibleFBT method calls dfs on the input number of nodes n, and returns the resulting list of all possible full binary trees with n nodes.
# This method uses a dynamic programming approach to solve the problem, which involves breaking the problem down into smaller subproblems, solving each subproblem only once, and storing their results in a data structure (in this case, the dp dictionary). 
# The solution to the original problem is then computed from the solutions to the subproblems. This approach ensures that each subproblem is solved only once, reducing the time complexity of the algorithm.