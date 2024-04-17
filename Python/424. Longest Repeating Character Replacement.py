# 424. Longest Repeating Character Replacement

# Medium

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        
        count = {}
        l= 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l +=1
            res = max(res, r-l+1)
        return res

# Here’s a brief explanation of the code:

# res is an integer that stores the length of the longest substring.
# count is a dictionary that stores the frequency of each character in the current substring.
# l is the left pointer of the sliding window.
# The loop iterates over the string s with r as the right pointer of the sliding window.
# For each character s[r], it increments its count in the count dictionary.
# If the length of the current substring (r - l + 1) minus the count of the most frequent character max(count.values()) is greater than k, it means we need to replace more than k characters to make the substring consist of a single character. So, we decrement the count of the character at the left pointer s[l] and increment the left pointer l.
# After the while loop, we update res to be the maximum of res and the length of the current substring (r - l + 1).
# Finally, we return res.
# This solution has a time complexity of O(n) and a space complexity of O(1), 

# Here’s how the function works with these inputs:

# Initialize res = 0, count = {}, and l = 0.
# Iterate over the string with r ranging from 0 to 6.
# For each character, increment its count in count. After the first iteration, count = {'A': 1}.
# Check if (r - l + 1) - max(count.values()) > k. If it is, decrement the count of s[l] and increment l. In the first iteration, this condition is not met.
# Update res to be the maximum of res and r - l + 1. After the first iteration, res = 1.
# Repeat steps 3-5 for the rest of the string. The count dictionary and the l pointer are updated as necessary to ensure that we can replace at most k characters to make the substring consist of a single character.
# After all iterations, res is 4, which is the length of the longest substring that can be made by replacing at most k characters. So, the function returns 4.