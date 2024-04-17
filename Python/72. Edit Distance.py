# 72. Edit Distance

# Medium

# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character
 

# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
 

# Constraints:

# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for j in range(len(word2) + 1):   # Bottom row
            cache[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):    # left most column
            cache[i][len(word2)] = len(word1) - i

        for i in range(len(word1) -1, -1, -1):
            for j in range(len(word2) -1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = 1 + min(cache[i+1][j], cache[i][j+1], cache[i+1][j+1])   # Delete, insert, replace

        return cache[0][0]

        # @cache
        # def dfs(i, j):
        #     if i<0:
        #         return j+1
        #     if j<0:
        #         return i+1
        #     if word1[i] == word2[j]:
        #         return dfs(i-1, j-1)
        #     return min(dfs(i-1, j), dfs(i-1, j-1), dfs(i, j-1))+1
        # return dfs(len(word1)-1, len(word2)-1)
        
# Here’s how the code works:

# It initializes a 2D list cache with dimensions (len(word1) + 1) x (len(word2) + 1), filled with infinity (float("inf")). This list will be used to store the minimum number of operations required to transform substrings of word1 and word2.
# It fills the last row and the last column of cache with the number of operations required to transform a substring of word1 or word2 into an empty string, which is just the length of the substring.
# It then fills the rest of cache in a bottom-up manner, starting from the second last row and the second last column. For each cell cache[i][j], it checks if word1[i] is equal to word2[j]. If they are equal, it sets cache[i][j] to cache[i+1][j+1], because no operation is required to match the two characters. If they are not equal, it sets cache[i][j] to 1 + min(cache[i+1][j], cache[i][j+1], cache[i+1][j+1]), which represents the minimum number of operations required to transform word1[i:] into word2[j:].
# Finally, it returns cache[0][0], which represents the minimum number of operations required to transform word1 into word2.
# For example, if word1 = "horse" and word2 = "ros", the output of the function is 3, because it takes three operations to transform “horse” into “ros”: replace ‘h’ with ‘r’, remove ‘o’, and remove ‘e’