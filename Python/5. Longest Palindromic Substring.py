# 5.Longest Palindromic Substring

# Medium

# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s: str) -> str:
    
    # Naive approach   Runtime: 271ms
        res = ""
        
        for i in range(len(s)):
            # Odd length position
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            
            # Even position lenght
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    def helper(self, s, l, r):
        while l>=0 and r<len(s) and s[l] == s[r]:
            l-=1
            r+=1
        return s[l+1: r]

# Here’s a breakdown of the code:

# The longestPalindrome function is the main function. It initializes an empty string res to store the result.
# It then iterates over each character in the input string s. For each character, it checks for two possible palindromes:
# An odd-length palindrome centered at the current character.
# An even-length palindrome centered between the current character and the next character.
# To check for these palindromes, it calls the helper function with the appropriate parameters. The helper function expands outwards from the center and returns the longest palindrome it can find.
# If the palindrome returned by the helper function is longer than the current result stored in res, it updates res.
# Finally, after checking all characters, it returns res, which will contain the longest palindromic substring found.
# The helper function takes three parameters: the string s, and two indices l and r. It expands the potential palindrome by moving l to the left and r to the right as long as the characters at these positions are equal and within the bounds of the string. When it can no longer expand, it returns the substring from l+1 to r, which is the longest palindrome it found.

# This approach is known as “expand around center” and it has a time complexity of O(n^2), where n is the length of the input string. This is because in the worst case scenario, we end up expanding around each character in the string. The space complexity is O(1) as we only use a constant amount of space to store our results.

# Dynamic programming approach  Run time: 2451ms
        # n = len(s)
        # dp = [[False]*n for _ in range(n)]
        # ans = ""
        
        # for l in range(n):
        #     for i in range(n-l):
        #         j = i + l
        #         if l < 2:
        #             dp[i][j] = (s[i] == s[j])
        #         else:
        #             dp[i][j] = (s[i] == s[j] and dp[i+1][j-1])
                
        #         if dp[i][j] and (l+1 > len(ans)):
        #             ans = s[i:j+1]
        
        # return ans

# Initialize a 2D array: Create a 2D boolean array dp of size n x n, where n is the length of the input string. The cell dp[i][j] will be True if the substring from index i to j in the string is a palindrome.
# Fill the diagonal: A single character is always a palindrome, so set dp[i][i] to True for all i.
# Consider substrings of length 2: Set dp[i][i+1] to True if the two characters at index i and i+1 are the same.
# Fill the rest of the table: Now, for substrings of length 3 and more, set dp[i][j] to True if dp[i+1][j-1] is True and the characters at index i and j are the same. This means that if the substring from index i+1 to j-1 is a palindrome and the characters at index i and j are the same, then the substring from index i to j is also a palindrome.
# Find the longest palindromic substring: Finally, iterate over the dp table to find the longest substring where dp[i][j] is True.