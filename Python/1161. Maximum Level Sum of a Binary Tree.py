# 1161. Maximum Level Sum of a Binary Tree

# Medium - Leetcode 75

# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

# Example 1:


# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.
# Example 2:

# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        # BFS METHOD:

        # maxx, lvl, maxlvl = -float('inf'), 0, 0
        # q = deque([root])

        # while q:
        #     sum = 0
        #     lvl += 1

        #     for i in range(len(q)):
        #         node = q.popleft()

        #         if node:
        #             sum += node.val
        #             if node.left: q.append(node.left)
        #             if node.right: q.append(node.right)
            
        #     if maxx < sum:
        #         maxx, maxlvl = sum, lvl

        # return maxlvl


        # DFS METHOD:

        def dfs(root, res, lvl):
            if not root: return

            if len(res) == lvl:
                res.append(root.val)
            else: 
                res[lvl] += root.val
                
            dfs(root.left, res,  lvl + 1)
            dfs(root.right, res, lvl + 1)

        res = []
        dfs(root,res, 0)
        return res.index(max(res)) + 1

