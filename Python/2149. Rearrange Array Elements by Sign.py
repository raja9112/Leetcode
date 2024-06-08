# 2149. Rearrange Array Elements by Sign

# Medium 

# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

# You should return the array of nums such that the the array follows the given conditions:

# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

 

# Example 1:

# Input: nums = [3,1,-2,-5,2,-4]
# Output: [3,-2,1,-5,2,-4]
# Explanation:
# The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
# The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
# Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  
# Example 2:

# Input: nums = [-1,1]
# Output: [1,-1]
# Explanation:
# 1 is the only positive integer and -1 the only negative integer in nums.
# So nums is rearranged to [1,-1].
 

# Constraints:

# 2 <= nums.length <= 2 * 105
# nums.length is even
# 1 <= |nums[i]| <= 105
# nums consists of equal number of positive and negative integers.
 

# It is not required to do the modifications in-place.

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        p, n = 0, 1
        for num in nums:
            if num > 0:
                res[p] = num
                p += 2
            else:
                res[n] = num
                n += 2
        return res
            

# Initialization:
# res is initialized to a list of zeros with the same length as nums.
# pos_index is initialized to 0 to keep track of the positions for positive numbers.
# neg_index is initialized to 1 to keep track of the positions for negative numbers.
      
# Loop through nums:
# If a number is positive, it is placed at the current pos_index, and pos_index is incremented by 2.
# If a number is negative, it is placed at the current neg_index, and neg_index is incremented by 2.
      
# Return the result:
# The res list is returned with positive numbers at even indices and negative numbers at odd indices.

# Complexity
# Space = O(n)
# Time = O(n)
