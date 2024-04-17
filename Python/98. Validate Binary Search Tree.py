# 98. Validate Binary Search Tree

# Medium

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left 
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [2,1,3]
# Output: true
# Example 2:


# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def help(root, left, right):
            if not root:
                return True
            
            if not (root.val > left and root.val < right):
                return False

            return help(root.left, left, root.val) and help(root.right, root.val, right)

        # float('inf') is used for setting a variable with an infinitely large value
        return help(root, float("-inf"), float("inf"))

# The logic of the function is as follows:

# It uses a helper function help that takes a node root and two values left and right as input.
# If root is None, it means we’ve reached a leaf node, so it returns True.
# If the value of root is not greater than left and less than right, it means the binary tree is not a BST, so it returns False.
# It then recursively calls help on the left and right children of root, updating the values of left and right to root.val.
# Finally, it calls help on the root of the binary tree with left as negative infinity and right as positive infinity.
# This solution works in O(n) time complexity, where n is the number of nodes in the binary tree. It doesn’t require any extra space, so the space complexity is O(1). This makes it an efficient solution for the problem.




