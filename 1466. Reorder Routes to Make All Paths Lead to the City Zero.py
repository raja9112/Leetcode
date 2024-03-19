# 1466. Reorder Routes to Make All Paths Lead to the City Zero

# Medium

# There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

# Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

# This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

# Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

# It's guaranteed that each city can reach city 0 after reorder.

 

# Example 1:


# Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# Output: 3
# Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
# Example 2:


# Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
# Output: 2
# Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
# Example 3:

# Input: n = 3, connections = [[1,0],[2,0]]
# Output: 0
 

# Constraints:

# 2 <= n <= 5 * 104
# connections.length == n - 1
# connections[i].length == 2
# 0 <= ai, bi <= n - 1
# ai != bi

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = { (a, b) for a, b in connections}       # {(0, 1), (4, 0), (2, 3), (4, 5), (1, 3)}
        neighbors = { city: [] for city in range(n)}

        visit = set()
        changes = 0

        for a, b in connections:        # {0: [1, 4], 1: [0, 3], 2: [3], 3: [1, 2], 4: [0, 5], 5: [4]}
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(city):
            nonlocal edges, neighbors, visit, changes

            for neighbor in neighbors[city]:
                if neighbor in visit:
                    continue

                if (neighbor, city ) not in edges:
                    changes+=1
                visit.add(neighbor)
                dfs(neighbor)
        visit.add(0)
        dfs(0)
        return changes
    
# Here’s a step-by-step explanation of the code:

# Initialization: The edges set stores all the directed edges in the graph. The neighbors dictionary stores the neighbors of each node. The visit set will store the nodes that have been visited during the depth-first search (DFS). The changes variable keeps track of the number of changes needed.
# Building the Graph: The program then iterates over all the connections. For each connection from a to b, it adds b to the list of a’s neighbors and a to the list of b’s neighbors.
# Depth-First Search (DFS): The dfs function is defined to perform a DFS on the graph. It takes a node city as an argument. For each neighbor of city, if the neighbor has not been visited, it checks if the edge from city to neighbor exists in the edges set. If it doesn’t, it means that the edge needs to be reversed for the graph to be reachable from the root, so it increments changes. It then adds neighbor to the visit set and recursively calls dfs on neighbor.
# Execution: The DFS is started from the root node (node 0). The number of changes needed is then returned.

# In the code, neighbors is a dictionary where each key is a city (or node in the graph), and the value is a list of all the cities (or nodes) that are directly connected to it.
# When you see neighbors[city] in the code, it’s accessing the list of all cities (or nodes) that are directly connected to the city specified by city.
# For example, if city = 1 and neighbors = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}, then neighbors[city] would give you [0, 3], which are the cities directly connected to city 1.