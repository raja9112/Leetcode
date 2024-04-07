# 691. Stickers to Spell Word

# Hard

# We are given n different types of stickers. Each sticker has a lowercase English word on it.

# You would like to spell out the given string target by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

# Return the minimum number of stickers that you need to spell out target. If the task is impossible, return -1.

# Note: In all test cases, all words were chosen randomly from the 1000 most common US English words, and target was chosen as a concatenation of two random words.

 

# Example 1:

# Input: stickers = ["with","example","science"], target = "thehat"
# Output: 3
# Explanation:
# We can use 2 "with" stickers, and 1 "example" sticker.
# After cutting and rearrange the letters of those stickers, we can form the target "thehat".
# Also, this is the minimum number of stickers necessary to form the target string.
# Example 2:

# Input: stickers = ["notice","possible"], target = "basicbasic"
# Output: -1
# Explanation:
# We cannot form the target "basicbasic" from cutting letters from the given stickers.
 

# Constraints:

# n == stickers.length
# 1 <= n <= 50
# 1 <= stickers[i].length <= 10
# 1 <= target.length <= 15
# stickers[i] and target consist of lowercase English letters.

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        stickCount = []
        for i, s in enumerate(stickers):
            stickCount.append({})
            for c in s:
                stickCount[i][c] = 1+ stickCount[i].get(c, 0)


        dp = {}  # key: subsequence of the target | value: min num of stickers
        def dfs(t, stick):
            if t in dp:
                return dp[t]

            res = 1 if stick else 0
            remainT = ""
            for c in t:
                if c in stick and stick[c] >0:
                    stick[c] -= 1
                else:
                    remainT += c

            if remainT:
                used = float("inf")

                for s in stickCount:
                    if remainT[0] not in s:
                        continue
                    used = min(used, dfs(remainT, s.copy()))
                dp[remainT] = used
                res += used
            return res


        res = dfs(target, {})
        return res if res != float("inf") else -1

# Here’s a step-by-step explanation of the code:

# stickCount: This is a list of dictionaries. Each dictionary corresponds to a sticker and maps each character in the sticker to its frequency in the sticker.
# dp: This is a dictionary that will store the minimum number of stickers required for each subsequence of the target string.
# dfs function: This is a helper function that uses depth-first search to find the minimum number of stickers required for a given target string t and a given sticker stick.
# If t is already in dp, it returns the stored value.
# It initializes res to 1 if stick is not empty, and 0 otherwise. It also initializes remainT to an empty string.
# It then iterates over each character c in t. If c is in stick and its count is greater than 0, it decreases the count by 1. Otherwise, it adds c to remainT.
# If remainT is not empty, it initializes used to infinity and then iterates over each sticker s in stickCount. If the first character of remainT is not in s, it continues to the next sticker. Otherwise, it updates used to the minimum of its current value and the result of the recursive call to dfs on remainT and a copy of s. It then stores used in dp[remainT] and adds used to res.
# Finally, it returns res.
# The minStickers method calls dfs on the target string and an empty dictionary, and stores the result in res. It then returns res if res is not infinity, and -1 otherwise.