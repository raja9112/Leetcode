# 1888. Minimum Number of Flips to Make the Binary String Alternating
# Medium

# You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

# Type-1: Remove the character at the start of the string s and append it to the end of the string.
# Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
# Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

# The string is called alternating if no two adjacent characters are equal.

# For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
 

# Example 1:

# Input: s = "111000"
# Output: 2
# Explanation: Use the first operation two times to make s = "100011".
# Then, use the second operation on the third and sixth elements to make s = "101010".
# Example 2:

# Input: s = "010"
# Output: 0
# Explanation: The string is already alternating.
# Example 3:

# Input: s = "1110"
# Output: 1
# Explanation: Use the second operation on the second element to make s = "1010".
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is either '0' or '1'.


class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        alt1 = alt2 = ""
        
        for i in range(len(s)):
            alt1 += "1" if i%2 else "0"
            alt2 += "0" if i%2 else "1"

        res = len(s)
        dif1 = dif2 = 0
        l = 0
        for r in range(len(s)):
            if s[r] != alt1[r]:
                dif1 += 1
            if s[r] != alt2[r]:
                dif2 += 1

            if (r - l + 1) > n:
                if s[l] != alt1[l]:
                    dif1 -= 1
                if s[l] != alt2[l]:
                    dif2 -= 1
                l += 1

            if (r - l + 1) == n:
                res = min(res, dif1, dif2)

        return res

# Here's a step-by-step explanation of how the code works:

# It initializes some variables:

# n represents the length of the input string s.
# s is duplicated and stored in itself (s = s + s). This duplication facilitates handling circular substrings.
# It generates two alternate patterns alt1 and alt2 by iterating through the extended string s and appending '0's and '1's alternatively based on the index:

# alt1 has '0's at even indices and '1's at odd indices.
# alt2 has '1's at even indices and '0's at odd indices.
# It initializes variables:

# res is initialized to the length of the string s, representing the worst-case scenario where every character needs to be flipped.
# dif1 and dif2 represent the differences between s and the alternate patterns alt1 and alt2 respectively.
# l and r are pointers representing the left and right ends of the sliding window.
# It iterates through the extended string s using the sliding window approach, where r moves forward to expand the window and l moves forward to contract the window when it exceeds the length of the original string s.

# At each step of the iteration, it calculates dif1 and dif2 by comparing the characters of s with the corresponding characters in the alternate patterns alt1 and alt2.

# When the length of the current window equals the length of the original string s, it updates the res variable to the minimum of the current value of res, dif1, and dif2.

# Finally, it returns the minimum of res, dif1, and dif2, representing the minimum number of flips required to achieve the desired pattern.

# Let's compute an example input to understand how the computation works:

# Consider the input string s = "00110":

# After duplication, s becomes "0011000110".
# Alternate patterns alt1 and alt2 are "0101010101" and "1010101010" respectively.
# During the iteration, the sliding window considers substrings like "001100", "011000", "110001", "100011", etc.
# At each step, it calculates the differences between the substring and the alternate patterns.
# After completing the iteration, it returns the minimum number of flips required.