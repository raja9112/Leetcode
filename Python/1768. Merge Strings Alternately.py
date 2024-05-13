# 1768. Merge Strings Alternately

# EASY

# LEETCODE 75

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

 

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
 

# Constraints:

# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # res = []
        # i = 0

        # while i < len(word1) or i < len(word2):
        #     if i < len(word1):
        #         res.append(word1[i])
        #     if i < len(word2):
        #         res.append(word2[i])
        #     i+= 1

        # return ''.join(res)

        res = ""
        i = 0

        while i < len(word1) or i < len(word2):
            if i < len(word1):
                res += word1[i]
            if i < len(word2):
                res += word2[i]
            i+= 1

        return res

# Approach
# Here’s a step-by-step explanation:

# It initializes an empty list res and a counter i at 0.
# It enters a loop that continues as long as i is less than the length of either word1 or word2.
# Inside the loop, if i is less than the length of word1, it appends the i-th character of word1 to res.
# Similarly, if i is less than the length of word2, it appends the i-th character of word2 to res.
# It increments i by 1 at the end of each loop iteration.
# After the loop, it joins the characters in res into a single string and returns it.
# Complexity
# Time complexity: O(n)
# Space complexity:O(n)