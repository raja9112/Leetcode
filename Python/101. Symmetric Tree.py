# 101. Symmetric Tree
# Solved
# Easy
# Topics
# Companies
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

# Example 1:


# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:


# Input: root = [1,2,2,null,3,null,3]
# Output: false
 

# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
 

# Follow up: Could you solve it both recursively and iteratively?


# Resursive method
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return False

        return self.result(root.left, root.right)

    def result(self, leftroot, rightroot):

        if leftroot == None and rightroot == None:
            return True

        if leftroot == None or rightroot == None:
            return False
        
        if leftroot.val != rightroot.val:
            return False

        return self.result(leftroot.left, rightroot.right) and self.result(leftroot.right, rightroot.left)


