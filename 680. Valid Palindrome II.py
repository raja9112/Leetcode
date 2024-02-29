# 680. Valid Palindrome II

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l <= r:
            if s[l] != s[r]:
                skipL, skipR = s[l + 1:r + 1], s[l:r]
                return (skipL == skipL[::-1] or skipR == skipR[::-1])
            l, r = l + 1, r - 1
        return True

#  let’s break down how the validPalindrome function works with the input s = "abca".

# Initialization: The input s is "abca". We initialize l to 0, r to 3, and res to 0.
# Iteration:
# For the first iteration, we compare s[l] and s[r], which are "a" and "a". Since they are the same, we move the pointers one step towards each other, so l becomes 1 and r becomes 2.
# For the second iteration, we compare s[l] and s[r], which are "b" and "c". Since they are not the same, we create skipL and skipR, which are "ca" and "b".
# We then check if either skipL or skipR is a palindrome. Since "ca" is not a palindrome and "b" is a palindrome, we return True.
# So, the output is True, which means the string "abca" can become a palindrome by removing at most one character.