# 230. Kth Smallest Element in a BST

# Medium

# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

# Example 1:


# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
 

# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []  # Initialize an empty stack.
        curr = root  # Start from the root of the tree.

        while curr or stack:  # Continue until there are no more nodes to visit.
            while curr:  # Go to the leftmost node of the current subtree.
                stack.append(curr)  # Add the node to the stack before going to its left child.
                curr = curr.left

            curr = stack.pop()  # Backtrack from the empty subtree and visit the node at the top of the stack.
            k -= 1  # Decrease k because we have visited one more node.
            if k == 0:  # If we've visited k nodes, then the current node is the kth smallest node.
                return curr.val  # Return its value.
            curr = curr.right  # Visit the right child.
