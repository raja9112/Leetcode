# 91. Decode Ways

# Medium

# A message containing letters from A-Z can be encoded into numbers using the following mapping:

# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

# Given a string s containing only digits, return the number of ways to decode it.

# The test cases are generated so that the answer fits in a 32-bit integer.

 

# Example 1:

# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
# Example 2:

# Input: s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
# Example 3:

# Input: s = "06"
# Output: 0
# Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
 

# Constraints:

# 1 <= s.length <= 100
# s contains only digits and may contain leading zero(s).

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else: dp[i] = dp[i+1]

            if (i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                dp[i] += dp[i+2]

        return dp[0]

# This is a Python solution for the problem of decoding a message. The problem is based on the idea that each number from ‘1’ to ‘26’ can be mapped to a letter of the alphabet, and you are given a string of digits and need to determine the total number of ways it can be decoded.
# The function numDecodings takes a string s as input and returns the total number of ways the string can be decoded.
# The solution uses dynamic programming to solve the problem. It initializes a dictionary dp where the key is the index in the string and the value is the number of ways the substring from that index can be decoded. The base case is that there is one way to decode an empty string, so dp[len(s)] is set to 1.
# The function then iterates over the string from right to left. If the current character is ‘0’, there are no ways to decode it, so dp[i] is set to 0. Otherwise, dp[i] is set to dp[i + 1] because the current character can be decoded in the same ways as the rest of the string.
# The function also checks if the current character and the next character form a valid two-digit number that can be decoded (i.e., ‘10’ to ‘26’). If they do, dp[i] is incremented by dp[i + 2] because these two characters can be decoded in the same ways as the string after them.
# Finally, the function returns dp[0], which is the total number of ways the entire string can be decoded.
# This solution has a time complexity of O(n) and a space complexity of O(n)

# let’s take an example input string “123” and see how it’s processed by the numDecodings function.

# Here’s a step-by-step breakdown:
# Initialize the dp dictionary with dp[len(s)] = 1. In this case, dp[3] = 1.
# Start iterating from the end of the string. The loop variable i goes from 2 to 0.
# For i = 2, s[i] is “3”. Since it’s not “0”, dp[i] is set to dp[i + 1], which is dp[3] = 1. The two-digit number formed by “3” and the next character doesn’t exist, so dp[i] remains 1.
# For i = 1, s[i] is “2”. Again, dp[i] is set to dp[i + 1], which is dp[2] = 1. The two-digit number formed by “2” and the next character “3” is “23”, which is valid, so dp[i] is incremented by dp[i + 2], which is dp[3] = 1. Now, dp[i] = 2.
# For i = 0, s[i] is “1”. dp[i] is set to dp[i + 1], which is dp[1] = 2. The two-digit number formed by “1” and the next character “2” is “12”, which is valid, so dp[i] is incremented by dp[i + 2], which is dp[2] = 1. Now, dp[i] = 3.
# Finally, return dp[0], which is 3.
# So, the string “123” can be decoded in 3 ways: “ABC”, “LC”, and “AW”.
