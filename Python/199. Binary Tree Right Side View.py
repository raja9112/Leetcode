# 199. Binary Tree Right Side View

# Medium - leetcode 75

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

# Example 1:


# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Example 2:

# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []

        # DFS Method
        
        # def dfs(root, lvl):
        #     if not root:
        #         return 

        #     if len(self.res) == lvl: self.res.append(root.val)

        #     dfs(root.right, lvl + 1)
        #     dfs(root.left, lvl + 1)

            
        # dfs(root, 0)
        # return self.res

        # Method 2: BFS
        q = deque([root])
        while q:
            rightmost = None
                
            for i in range(len(q)):
                node = q.popleft()

                if node:
                    rightmost = node
                    q.append(node.left)
                    q.append(node.right)

            if rightmost: self.res.append(rightmost.val)

        return self.res
                
        # First root node 1 will be there in q
        # q is non empty so while loop starts, and assigns rightmost as None
        # using for loop at the range of len(q) that means 1
        # poping leftmost from q for 1 time, as the len(q) in iteration and assign it to node variable
        # if node is non empty, then assign rightmost as node and appending node's left and right child to q
        # after iteration ends, the rightmost appended to q
        # Iteration 2: this time 2 nodes (2, 3) will be inside q, so there will be a 2 iterations will happen in for loop
        # left node (2) will assigned as rightmost first, but in the second iteration it will change to node(3)
        # so it will append the node(3) as the rightmost to res
            