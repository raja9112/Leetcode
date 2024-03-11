# 131. Palindrome Partitioning

# Medium

# Given a string s, partition s such that every 
# substring
#  of the partition is a 
# palindrome
# . Return all possible palindrome partitioning of s.

 

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]
 

# Constraints:

# 1 <= s.length <= 16
# s contains only lowercase English letters.

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())

            for j in range(i, len(s)):
                if self.ispali(s, i, j):
                    part.append(s[i: j+1])
                    dfs(j+1)
                    part.pop()

        dfs(0)
        return res

    def ispali(self, s, l, r):
        while l<r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True

# The partition method takes a string s as input and returns a list of all possible palindromic partitions of s. It uses depth-first search (DFS) to explore all possible partitions.

# The ispali method checks if a substring of s (specified by the left and right indices l and r) is a palindrome. It returns True if the substring is a palindrome and False otherwise.

# Here’s a brief explanation of the code:

# res is a list that stores all the palindromic partitions.
# part is a list that stores the current partition.
# The dfs function is a helper function that performs DFS on the string. It starts from the index i and explores all possible partitions.
# If i is greater than or equal to the length of s, it means we have found a valid partition, so we add a copy of part to res.
# For each index j from i to the end of s, if the substring s[i:j+1] is a palindrome (checked using the ispali method), we add it to part and recursively call dfs with the next index j+1. After the recursive call, we remove the last element from part to backtrack and explore other partitions.
# Finally, we call dfs with the initial index 0 and return res.
# This solution has a time complexity of O(N*2^N) and a space complexity of O(N^2), where N is the length of the string s. This is because in the worst case, we could end up exploring all possible partitions of the string. 
