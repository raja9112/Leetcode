# 49. Group Anagrams

# Medium

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26  # a.....z

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()

# Here’s a brief explanation:

# Initialization: The program first initializes a default dictionary res where each key is a tuple of 26 integers representing the count of each letter in a string, and the value is a list of strings that are anagrams of each other.
# Counting Letters: For each string s in the input list strs, it initializes a list count of 26 zeros representing the count of each letter in s. It then iterates over each character c in s, and increments the count of c in count.
# Grouping Anagrams: It then adds s to the list of anagrams in res that have the same letter count. The letter count is converted to a tuple to be used as a key in res.
# Returning Result: Finally, it returns the lists of anagrams in res.

