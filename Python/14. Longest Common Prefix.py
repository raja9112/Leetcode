class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for j in strs:
                if i == len(strs) or j[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
    
strs = ["flower","flow","flight"]
obj = Solution()
print(obj.longestCommonPrefix(strs))

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.