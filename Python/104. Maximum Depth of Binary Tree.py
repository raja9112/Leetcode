# 104. Maximum Depth of Binary Tree

# Easy - Leetcode 75

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if root:
        #     queue = deque([root])
        #     num_level = 1
        #     level = 0

        #     while queue:
        #         node = queue.popleft()

        #         if node.left: queue.append(node.left)
        #         if node.right: queue.append(node.right)
        #         num_level -= 1

        #         if num_level == 0:
        #             level += 1
        #             num_level = len(queue)
        #     return level

        # return 0

        if root:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        return 0
