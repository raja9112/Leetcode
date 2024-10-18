# 1081. Smallest Subsequence of Distinct Characters

# Medium

# Given a string s, return the 
# lexicographically smallest
 
# subsequence
#  of s that contains all the distinct characters of s exactly once.

 

# Example 1:

# Input: s = "bcabc"
# Output: "abc"
# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of lowercase English letters.
 

# Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/



class Solution:
    def smallestSubsequence(self, s: str) -> str:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else: d[i] = 1


        stack = []
        seen = set()

        for ch in s:
            d[ch] -= 1
            
            if ch not in stack:
                while stack and stack[-1] > ch and d[stack[-1]] > 0:
                    seen.remove(stack.pop())

                stack.append(ch)
                seen.add(ch)
        return "".join(stack)
            