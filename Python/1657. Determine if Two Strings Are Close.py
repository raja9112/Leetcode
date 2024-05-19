# 1657. Determine if Two Strings Are Close

# Medium - Leetcode 75

# Two strings are considered close if you can attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

 

# Example 1:

# Input: word1 = "abc", word2 = "bca"
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"
# Example 2:

# Input: word1 = "a", word2 = "aa"
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
# Example 3:

# Input: word1 = "cabbba", word2 = "abbccc"
# Output: true
# Explanation: You can attain word2 from word1 in 3 operations.
# Apply Operation 1: "cabbba" -> "caabbb"
# Apply Operation 2: "caabbb" -> "baaccc"
# Apply Operation 2: "baaccc" -> "abbccc"
 

# Constraints:

# 1 <= word1.length, word2.length <= 105
# word1 and word2 contain only lowercase English letters.

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = [0] * 26
        freq2 = [0] * 26

        for ch in word1:
            freq1[ord(ch) - ord('a')] += 1

        for ch in word2:
            freq2[ord(ch) - ord('a')] += 1

        for i in range(26):
            if (freq1[i] == 0 and freq2[i] != 0) or (freq2[i] == 0 and freq1[i] != 0):
                return False
        
        freq1.sort()
        freq2.sort()

        for i in range(26):
            if (freq1[i] != freq2[i]):
                return False
        return True


        # Method 2
        # c1 = Counter(word1)
        # c2 = Counter(word2)
        
        # return sorted(c1.values()) == sorted(c2.values()) and set(c1.keys()) == set(c2.keys())

        # Method 3
        # if len(word1) != len(word2): return False
        # arr1 = []
        # arr2 = []
        # for j in set(word1):
        #     arr1.append(word1.count(j))
        #     arr2.append(word2.count(j))
        # arr1.sort()
        # arr2.sort()
        # return arr1 == arr2