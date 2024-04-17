# 105. Construct Binary Tree from Preorder and Inorder Traversal

# Medium

# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:


# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
 

# Constraints:

# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])

        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1: mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1: ], inorder[mid+1:])
        return root

# The buildTree function takes two lists as input: preorder and inorder. It starts by checking if these lists are empty. If they are, it returns None, indicating that the tree cannot be built.
# If the lists are not empty, the function creates a new TreeNode with the value of the first element in the preorder list (which is the root of the tree).
# The function then finds the position of the root in the inorder list. This position (mid) divides the inorder list into two halves: the left half contains elements of the left subtree, and the right half contains elements of the right subtree.
# The function then recursively calls itself to construct the left and right subtrees. For the left subtree, it uses the elements from the start of the lists to mid, and for the right subtree, it uses the elements from mid+1 to the end of the lists.
# Finally, the function returns the root node of the constructed tree.