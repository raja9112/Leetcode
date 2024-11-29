# 111. Minimum Depth of Binary Tree

# EASY

# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 2
# Example 2:

# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
 

# Constraints:

# The number of nodes in the tree is in the range [0, 105].
# -1000 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        # def helper(node, depth):
            # if node is None:
            #     return float('inf')

            # if not node.left and not node.right:
            #     return depth

            # left_depth = helper(node.left, depth + 1)
            # right_depth = helper(node.right, depth + 1)

            # return min(left_depth, right_depth)

        # if root is None:
        #     return 0
        # return helper(root, 1)


        def helper(node):
            if node is None:
                return 0

            if node.left is None:
                return 1 + helper(node.right)
            if node.right is None:
                return 1 + helper(node.left)
            
            return 1 + min(helper(node.left), helper(node.right))

        if root is None:
            return 0
        return helper(root)