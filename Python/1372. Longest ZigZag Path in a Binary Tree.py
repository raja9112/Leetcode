# 1372. Longest ZigZag Path in a Binary Tree

# Medium - Leetcode 75

# You are given the root of a binary tree.

# A ZigZag path for a binary tree is defined as follow:

# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
# Change the direction from right to left or from left to right.
# Repeat the second and third steps until you can't move in the tree.
# Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

# Return the longest ZigZag path contained in that tree.

 

# Example 1:


# Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
# Output: 3
# Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
# Example 2:


# Input: root = [1,1,1,null,1,null,null,1,1,null,1]
# Output: 4
# Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
# Example 3:

# Input: root = [1]
# Output: 0
 

# Constraints:

# The number of nodes in the tree is in the range [1, 5 * 104].
# 1 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        self.maxCount = 0

        def dfs(node, dir, count):
            self.maxCount = max(self.maxCount, count)

            if node.right:
                if dir == "left":
                    dfs(node.right, "right", count + 1)
                else: dfs(node.right, "right", 1)

            if node.left:
                if dir == "right":
                    dfs(node.left, "left", count + 1)
                else: dfs(node.left, "left", 1)


        dfs(root, "", 0)
        return self.maxCount
    
# Step-by-Step Computation
# Initialization:

# self.maxCount is initialized to 0. This variable keeps track of the maximum length of any ZigZag path found during the traversal.
# Depth-First Search (DFS) Function:

# A helper function dfs is defined within longestZigZag. This function takes three arguments:
# node: The current node being processed.
# dir: A string indicating the direction from the parent node ("left" or "right").
# count: The current length of the ZigZag path ending at the current node.
# Processing Each Node:

# For the current node, self.maxCount is updated to be the maximum of its current value and count, which represents the length of the current ZigZag path.
# If the current node has a right child:
# If the direction from the parent was "left", this means the path continues in a ZigZag manner, so the count is incremented by 1.
# Otherwise, if the direction from the parent was "right", the path does not continue in a ZigZag manner, so the count is reset to 1.
# The dfs function is then recursively called on the right child with the appropriate parameters.
# If the current node has a left child:
# If the direction from the parent was "right", the path continues in a ZigZag manner, so the count is incremented by 1.
# Otherwise, if the direction from the parent was "left", the path does not continue in a ZigZag manner, so the count is reset to 1.
# The dfs function is then recursively called on the left child with the appropriate parameters.
# Start and Return:

# The DFS traversal is initiated by calling dfs(root, "", 0) from the root node with an initial direction as an empty string and a count of 0.
# The function returns self.maxCount, which contains the length of the longest ZigZag path found.
# Computational Complexity
# Time Complexity: O(N), where N is the number of nodes in the tree. This is because each node is visited exactly once.
# Space Complexity: O(H), where H is the height of the tree. This is due to the space used by the recursion stack. In the worst case (completely unbalanced tree), the height H can be equal to N, leading to a space complexity of O(N).