# 10. Regular Expression Matching

# Hard

# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

 

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:

# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
 

# Constraints:

# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        cache = {}        
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if (j+1) < len(p) and p[j+1] == "*":
                cache[(i, j)] = (dfs(i, j+2) or (match and dfs(i+1, j)))
                return cache[(i, j)]

            if match:
                cache[(i, j)] = dfs(i+1, j+1)
                return cache[(i, j)]

            cache[(i, j)] = False
            return cache[(i, j)]

        return dfs(0, 0)

# Here’s how the code works:

# It defines a helper function dfs(i, j) that checks if the substring of s starting at index i matches the substring of p starting at index j. This function uses a cache to store the results of previous computations, which improves efficiency.
# If the current state (i, j) is in the cache, it returns the cached result. If i is beyond the end of s and j is beyond the end of p, it returns True, because two empty strings match. If j is beyond the end of p but i is not beyond the end of s, it returns False, because a non-empty string cannot match an empty pattern.
# It checks if the current characters of s and p match. They match if they are the same or if the current character of p is ..
# If the next character of p is *, it checks if the rest of s matches either the rest of p after skipping the current character and *, or the rest of p without skipping if the current characters of s and p match.
# If the current characters of s and p match and the next character of p is not *, it checks if the rest of s matches the rest of p.
# If none of the above conditions are met, it returns False.
# Finally, it calls dfs(0, 0) to check if s matches p from the beginning.
# This solution has a time complexity of O(sp), where s and p are the lengths of the string and the pattern, respectively. The space complexity is also O(sp), due to the cache used for memoization.