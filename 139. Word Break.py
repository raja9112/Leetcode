# 139. Word Break

# Medium

# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
 

# Constraints:

# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i+len(w) <= len(s) and s[i: i+len(w)] == w):
                    dp[i] = dp[i+len(w)]

                if dp[i]:
                    break
        return dp[0]

# Here’s a step-by-step explanation:

# Initialization: A boolean list dp of size len(s)+1 is initialized with False. The last element dp[len(s)] is set to True. This list will be used to store whether a substring from the i-th index to the end can be segmented into words in the wordDict.
# Iterate over the string: The outer loop iterates over the string s in reverse order. For each character at index i, it checks every word w in wordDict.
# Check if a word can be formed: If a word w can be formed starting from the i-th index (i.e., s[i: i+len(w)] == w), then dp[i] is set to dp[i+len(w)]. This means that if the substring from i+len(w) to the end can be segmented into words in wordDict, then the substring from i to the end can also be segmented.
# Break the loop: If dp[i] is True, it breaks the inner loop. This is because we’ve found a word w that can be formed starting from the i-th index, so there’s no need to check the remaining words in wordDict.
# Return the result: Finally, it returns dp[0], which indicates whether the entire string s can be segmented into words in wordDict.
# This solution uses dynamic programming to reduce the time complexity. It solves the problem by breaking it down into smaller subproblems (i.e., whether a substring can be segmented), and stores the results of these subproblems to avoid redundant computation.

# let’s consider an example. Suppose we have the following input:

# Python

# s = "applepenapple"
# wordDict = ["apple", "pen"]

# Here’s how the program would work with this input:

# Initialization: dp is initialized as [False, False, False, False, False, False, False, False, False, False, False, False, False, True].
# Iterate over the string: The outer loop starts at index 12 (the second last index) and goes to index 0.
# Check if a word can be formed: For each index i, it checks every word in wordDict. If a word can be formed starting from the i-th index, then dp[i] is set to dp[i+len(w)]. For example, when i is 8 and w is “apple”, s[8: 8+len("apple")] is “apple”, so dp[8] is set to dp[13], which is True.
# Break the loop: If dp[i] is True, it breaks the inner loop. This happens when i is 8, because we’ve found that “apple” can be formed starting from the 8th index.
# Return the result: After the outer loop finishes, it returns dp[0], which is True. This means that the entire string “applepenapple” can be segmented into words in wordDict.
# So, for this input, the wordBreak method would return True, indicating that the string “applepenapple” can be segmented into words in wordDict.