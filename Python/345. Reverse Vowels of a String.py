# 345. Reverse Vowels of a String

# EASY - Leetcode 75

# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"
 

# Constraints:

# 1 <= s.length <= 3 * 105

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        r= len(s) - 1
        l=0
        vowels = "AEIOUaeiou"
        while l < r:
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
                l+=1
                r-=1

            elif s[l] in vowels:
                r -= 1
            elif s[l] not in vowels:
                l += 1

        return ''.join(s)
