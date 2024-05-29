# 547. Number of Provinces

# Medium - Leetcode 75

# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

 

# Example 1:


# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Example 2:


# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
 

# Constraints:

# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(start):
            visited.add(start)
            for end in range(len(isConnected)):
                if isConnected[start][end] and end not in visited:
                    dfs(end)

        provinces = 0
        visited = set()

        for start in range(len(isConnected)):
            if start not in visited:
                provinces += 1
                dfs(start)

        return provinces

# The findCircleNum function in the provided code determines the number of provinces (connected components) in an undirected graph represented by an adjacency matrix isConnected. 
# Each cell isConnected[i][j] is 1 if there is a direct connection between city i and city j, otherwise 0.

# Code Explanation
# Depth-First Search (DFS) Function:

# The dfs function is a helper function that performs a depth-first search starting from a given node (start).
# It marks the start node as visited.
# Then, it recursively visits all directly connected nodes (end) that haven't been visited yet.
# Main Logic:

# provinces is initialized to 0 to keep track of the number of connected components (provinces).
# visited is a set to keep track of all visited nodes.
# Iterate through each node (start). If the node hasn't been visited, it represents a new province. 
# Increment the provinces counter and call the dfs function starting from that node to visit all nodes in this province.

# Initialization:

# provinces = 0
# visited = set()

# First Iteration (start = 0):
    # Since City 0 is not visited, increment provinces to 1.
    # Call dfs(0):
    # Mark City 0 as visited (visited = {0}).
    # Check connections from City 0:
    # City 0 to City 0 (isConnected[0][0] = 1): Already visited.
    # City 0 to City 1 (isConnected[0][1] = 1): Not visited, call dfs(1):
    # Mark City 1 as visited (visited = {0, 1}).
    # Check connections from City 1:
    # City 1 to City 0 (isConnected[1][0] = 1): Already visited.
    # City 1 to City 1 (isConnected[1][1] = 1): Already visited.
    # City 1 to City 2 (isConnected[1][2] = 0): No connection.
    # Return from dfs(1).
    # Return from dfs(0).

# Second Iteration (start = 1):
    # Since City 1 is already visited, skip to the next iteration.
    # Third Iteration (start = 2):

    # Since City 2 is not visited, increment provinces to 2.
    # Call dfs(2):
    # Mark City 2 as visited (visited = {0, 1, 2}).
    # Check connections from City 2:
    # City 2 to City 0 (isConnected[2][0] = 0): No connection.
    # City 2 to City 1 (isConnected[2][1] = 0): No connection.
    # City 2 to City 2 (isConnected[2][2] = 1): Already visited.
    # Return from dfs(2).

# Completion:
# All cities are visited, and the final count of provinces is 2.