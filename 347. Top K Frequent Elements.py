# 347. Top K Frequent Elements

# Medium

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for i, c in count.items():
            freq[c].append(i)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        # With time Complexity 0(n)
        # With space Complexity 0(n) due to the use of hashmap

# Here's how the code works:

# It defines a class Solution with a method topKFrequent that takes two arguments: nums, which is a list of integers, and k, an integer representing the number of top frequent elements to return.

# It initializes an empty dictionary count to store the count of occurrences of each number in nums.

# It initializes a list of lists freq with a length of len(nums) + 1. This list will be used to store numbers grouped by their frequencies. Each index i in freq corresponds to the frequency of a number.

# It iterates through each number n in the list nums:

# It updates the count of occurrences of n in the count dictionary.
# For each number n, it appends n to the sublist in freq corresponding to its frequency.
# It initializes an empty list res to store the result.

# It iterates backward through the list freq starting from the highest frequencies (from len(freq)-1 down to 1):

# For each frequency i, it iterates through the numbers n in the sublist freq[i].
# It appends each number n to the result list res.
# If the length of res equals k, it means we have found the top k frequent elements, so it returns res.