# 97. Interleaving String

# Medium

# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

# An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
# substrings
#  respectively, such that:

# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.

 

# Example 1:


# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Explanation: One way to obtain s3 is:
# Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
# Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
# Since s3 can be obtained by interleaving s1 and s2, we return true.
# Example 2:

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.
# Example 3:

# Input: s1 = "", s2 = "", s3 = ""
# Output: true
 

# Constraints:

# 0 <= s1.length, s2.length <= 100
# 0 <= s3.length <= 200
# s1, s2, and s3 consist of lowercase English letters.
 
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}

        def dfs(i, j):
            if len(s1) + len(s2) != len(s3):
                return False
                
            if i == len(s1) and j == len(s2):
                return True

            if (i, j) in dp:
                return dp[(i, j)]

            if i < len(s1) and s1[i] == s3[i+j] and dfs(i+1, j):
                return True
            if j < len(s2) and s2[j] == s3[i+j] and dfs(i, j+1):
                return True

            dp[(i, j)] = False
            return False
        return dfs(0, 0)
    
# Here’s a step-by-step explanation of the code:

# Initialization: The program first initializes an empty dictionary dp to store the computed results for subproblems.
# Depth-First Search (DFS): The dfs function is defined to perform a DFS on the strings s1 and s2. It takes two indices i and j as arguments, which represent the current positions in s1 and s2 respectively.
# Base Cases: If the total length of s1 and s2 is not equal to the length of s3, it returns False because s3 cannot be an interleaving of s1 and s2. If both i and j have reached the end of s1 and s2 respectively, it returns True because all characters have been matched.
# Memoization: If the pair (i, j) is in dp, it means the subproblem has been solved before, so it returns the stored result.
# Recursive Cases: If the current character in s1 or s2 matches the corresponding character in s3, it recursively calls dfs on the next position. If either of the recursive calls returns True, it returns True.
# Update dp: If none of the above conditions are met, it means the current configuration cannot lead to a valid interleaving, so it updates dp[(i, j)] to False and returns False.
# Execution: The DFS is started from the beginning of s1 and s2 (i.e., i = 0 and j = 0). The final result is then returned.