# 102. Binary Tree Level Order Traversal

# Medium

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                res.append(level)

        return res

# Here's how the code works:

# It defines a class Solution with a method levelOrder that takes a root node of a binary tree as input and returns a list of lists containing the values of nodes at each level.

# Within the levelOrder method:

# It initializes an empty list res to store the result.
# It initializes a deque q (double-ended queue) to store nodes that need to be visited.
# It appends the root node to the deque.
# It enters a while loop that continues as long as there are nodes in the deque q.

# Inside the loop:

# It initializes an empty list level to store the values of nodes at the current level.
# It iterates through the nodes currently in the deque by using a for loop that iterates over the length of the deque. This ensures that we only process nodes at the current level.
# Within this loop, it dequeues a node from the left side of the deque (q.popleft()).
# If the dequeued node is not None, it appends its value to the level list and enqueues its left and right child nodes (if they exist) into the deque q.
# This effectively processes all nodes at the current level and enqueues their children for the next level.
# After processing all nodes at the current level, if the level list is not empty, it appends the level list to the result list res.

# Finally, it returns the result list res, which contains the values of nodes at each level of the binary tree in a level order traversal manner.
