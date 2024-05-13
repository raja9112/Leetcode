# 1071. Greatest Common Divisor of Strings

# EASY -> Leetcode 75

# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
 

# Constraints:

# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1 or not str2:
            return str1 if str1 else str2

        if len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)

        if str1[:len(str2)] == str2:
        # if str1.startswith(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)

        return ""

# Algorithm:
#         The gcd could be:
#                          - the shorter string, EX: gcd(ABCABC, ABC) >>> ABC
#                          - a substring of the shorter string started from its first element. EX: gcd(ABABAB, ABAB) >>> AB
        
#         - We start by finding the longer string
#         - we remove the shorter string from the longer one
#         - then recursively check the gdc of what is left from the the previous step and the shorter string
#         - if one of the strings becomes '' return True
#         Note: len(str1) should always be greater than len(str2) because we always remove str2 from str1
#         -----------------------------------
#         EX: gdc(str1=ABABAB, str2=ABAB):
#                 ABABAB - ABAB = AB
#                 gdc(AB, ABAB)  # swap the inputs so the lengthier one is the 1st argument
#                     gdc(ABAB, AB)
#                         ABAB - AB = AB
#                         gdc(AB, AB)
#                             AB - AB = ''
#                             gdc('', AB) >>> AB