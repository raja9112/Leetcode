# 110. Balanced Binary Tree

# Easy

# Given a binary tree, determine if it is 
# height-balanced
# .

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def helper(node):
            if node is None:
                return -1

            return max(helper(node.left),helper(node.right)) + 1


        left = helper(root.left)
        right = helper(root.right)

        if abs(left - right) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)


# Main Function (isBalanced):
# The isBalanced method starts by calculating the height of the left and right subtrees of the root node (3).

# 3. Left Subtree Calculation (helper(9)):
# The left child of node 3 is 9, which has no children (null on both sides).
# The helper function for 9 returns a height of 0:
# For both left and right children (null), the height is -1.
# Max height is max(-1, -1) + 1 = 0.

# 4. Right Subtree Calculation (helper(20)):
# The right child of node 3 is 20.
# The helper function calculates the heights of the left and right subtrees of 20.

# 5. Left Subtree of 20 (helper(15)):
# The left child of node 20 is 15, which has no children.
# The helper function returns a height of 0 for 15:
# For both left and right children (null), the height is -1.
# Max height is max(-1, -1) + 1 = 0.

# 6. Right Subtree of 20 (helper(7)):
# The right child of node 20 is 7, which also has no children.
# The helper function returns a height of 0 for 7:
# For both left and right children (null), the height is -1.
# Max height is max(-1, -1) + 1 = 0.

# 7. Height of 20:
# The heights of both left (15) and right (7) subtrees of 20 are 0.
# Height of node 20 is:
# Max height is max(0, 0) + 1 = 1.

# 8. Height of Root Node (3):
# The height of the left subtree of node 3 (rooted at 9) is 0.
# The height of the right subtree of node 3 (rooted at 20) is 1.
# The height difference is:
# abs(0 - 1) = 1 (within the allowed limit of 1).

# 9. Recursive Balance Check:
# The algorithm recursively checks if the subtrees rooted at 9 and 20 are balanced:
# isBalanced(9) returns True (since 9 has no children).
# isBalanced(20) returns True (as both its subtrees, 15 and 7, are balanced).

# 10. Final Output:
# Since all subtrees are balanced, the entire tree is balanced.
# Output is True
    