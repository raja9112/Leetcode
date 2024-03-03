# 3. Longest Substring Without Repeating Characters

# Medium

# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding windows approach
        charSet = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res

# Implementation.

# Here’s how the program works with this input:

# The lengthOfLongestSubstring function is called with “abcabcbb” as the input.
# The function initializes an empty set charSet to store the characters in the current substring, an integer res to store the length of the longest substring found so far, and an integer l to store the left boundary of the current substring.
# It then starts a loop that iterates over each character in the string “abcabcbb” by its index r. For each character, it does the following:
# If the character s[r] is already in charSet, it means that the current substring contains repeating characters. So it enters a while loop where it removes the character at the left boundary s[l] from charSet and moves the left boundary one step to the right by incrementing l. This process continues until s[r] is not in charSet.
# After the while loop, it adds s[r] to charSet and updates res to be the maximum of the current res and the length of the current substring r-l+1.
# Finally, after checking all characters, it returns res, which is the length of the longest substring without repeating characters.
# Let’s see how this works with the string “abcabcbb”:

# The first three characters ‘a’, ‘b’, ‘c’ are all different, so they are added to charSet and res becomes 3.
# The next character is ‘a’, which is already in charSet. So it enters the while loop, removes ‘a’ from charSet, and increments l. Now charSet is {‘b’, ‘c’} and l is 1.
# It then adds ‘a’ to charSet and updates res to be the maximum of 3 and r-l+1, which is 3.
# The process continues for the rest of the characters. In the end, res is 3, which is the length of the longest substring without repeating characters (“abc”).
