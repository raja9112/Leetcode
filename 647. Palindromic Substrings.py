# 647. Palindromic Substrings

# Medium

# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

 

# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of lowercase English letters.

class Solution:
    def countSubstrings(self, s: str) -> int:
        # res = 0

        # for i in range(len(s)):
        #     l = r = i
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         l-=1
        #         r+=1
        #         res+=1

        #     l= i
        #     r = i+1
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         l-=1
        #         r+=1
        #         res+=1

        # return res


        # Method 2
        res = 0

        for i in range(len(s)):
            res += self.countpali(s, i, i)
            res += self.countpali(s, i, i+1)

        return res

    def countpali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
                res+=1

        return res
    
    
# Here’s a step-by-step breakdown:

# Initialize res to 0. This variable keeps track of the total number of palindromic substrings.
# Iterate over each character in the string. For each character, do the following:
# Initialize two pointers l and r at the current character. These pointers will be used to expand around the current character and check for palindromic substrings.
# While l and r are valid indices in the string and the characters at these indices are the same, increment res and move l one step to the left and r one step to the right. This checks for odd-length palindromic substrings centered at the current character.
# Reset l to the current character and set r to the next character. Then, do the same expansion and checking as before. This checks for even-length palindromic substrings that start at the current character.
# After checking all characters, return res as the total number of palindromic substrings.
    
# Time complexity: O(n^2)
# Space complexity: O(1) 