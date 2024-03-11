# 133. Clone Graph

# Medium

# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
 

# Test case format:

# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

# Example 1:


# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# Example 2:


# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
# Example 3:

# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.
 

# Constraints:

# The number of nodes in the graph is in the range [0, 100].
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# There are no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given node.

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldTonew = {}
        def dfs(node):
            if node in oldTonew:
                return oldTonew[node]

            copy = Node(node.val)
            oldTonew[node] = copy

            for n in node.neighbors:
                copy.neighbors.append(dfs(n))

            return copy

        return dfs(node) if node else None

# Here’s a brief explanation of the code:

# If the input node is None, the function returns None.
# The dfs function is a helper function that performs DFS on the graph. It takes a node as input and returns a copy of the node.
# If the node is already in the oldTonew dictionary, it means the node has been visited and cloned, so it returns the cloned node.
# If the node is not in the oldTonew dictionary, it creates a new node copy with the same value as the input node and adds it to the oldTonew dictionary.
# It then iterates over the neighbors of the input node. For each neighbor, it recursively calls dfs and adds the cloned neighbor to the copy.neighbors list.
# Finally, it returns the cloned node copy.
# The cloneGraph method calls dfs with the input node and returns the cloned graph.
# This solution has a time complexity of O(n) and a space complexity of O(n), where n is the number of nodes in the graph. 