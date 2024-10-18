# 316. Remove Duplicate Letters

# Medium

# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
# the smallest in lexicographical order
#  among all possible results.

 

# Example 1:

# Input: s = "bcabc"
# Output: "abc"
# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"
 

# Constraints:

# 1 <= s.length <= 104
# s consists of lowercase English letters.
 

# Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else: 
                d[i] = 1

        stack = []
        seen = set()

        for c in s:
            d[c] -= 1

            if c not in seen:
                while stack and stack[-1] > c and d[stack[-1]] > 0:
                    seen.remove(stack.pop())

                stack.append(c)
                seen.add(c)

        return "".join(stack)