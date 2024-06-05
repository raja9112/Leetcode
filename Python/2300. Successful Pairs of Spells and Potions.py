# 2300. Successful Pairs of Spells and Potions

# Medium - leetcode 75

# You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

# You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

 

# Example 1:

# Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
# Output: [4,0,3]
# Explanation:
# - 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
# - 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
# - 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
# Thus, [4,0,3] is returned.
# Example 2:

# Input: spells = [3,1,2], potions = [8,5,8], success = 16
# Output: [2,0,2]
# Explanation:
# - 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
# - 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
# - 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful. 
# Thus, [2,0,2] is returned.
 

# Constraints:

# n == spells.length
# m == potions.length
# 1 <= n, m <= 105
# 1 <= spells[i], potions[i] <= 105
# 1 <= success <= 1010

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # res = []
        # spells = deque(spells)
        # while len(spells) > 0:
        #     a = spells.popleft()
        #     count = 0
        #     for i in potions:
        #         if i*a >= success:
        #             count += 1
        #     res.append(count)

        # return res


        n = len(spells)
        m = len(potions)
        potions.sort()
        res = []
        
        for s in spells:
            l, r = 0, m-1
            idx = m
            while l<=r:
                mid = (l+r) // 2
                if s*potions[mid] >= success:
                    r = mid-1
                    idx = mid
                else:
                    l = mid + 1

            res.append(m - idx)
        return res

                


# Explanation and Complexity

# Initialization and Sorting:
# We first calculate the lengths of the spells and potions lists (n and m respectively).
# We sort the potions list, which allows us to efficiently use binary search later.

# Processing Each Spell with Binary Search:
# For each spell in spells, we perform a binary search on the sorted potions list.
# The binary search finds the smallest index idx where the product of the spell and the potion is greater than or equal to the success threshold.
# If such an index is found, the number of successful pairs for that spell is m - idx (i.e., all potions from idx to the end meet the success condition).

# Time Complexity
# Sorting Potions:
# Sorting the potions list takes O(mlogm).

# Binary Search for Each Spell:
# Performing a binary search for each spell takes O(logm).
# Since there are n spells, this step takes O(nlogm).

# Overall Time Complexity
# The overall time complexity is: O(mlogm+nlogm)

# Space Complexity
# The space complexity is O(n+m):
# Sorting is done in place for the potions list, so no additional space is required beyond the original list size, O(m).
# The res list stores results for each spell, which requires O(n) space.

