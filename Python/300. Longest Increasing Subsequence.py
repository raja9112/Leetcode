class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP   runtimeL 1883ms
        # dp = [1] * len(nums)

        # for i in range(len(nums)-1, -1, -1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] < nums[j]:
        #             dp[i] = max(dp[i], 1+dp[j])
        # return max(dp)

# Here’s how the program works with this input:

# The lengthOfLIS function is called with [10, 9, 2, 5, 3, 7, 101, 18] as the input.
# The function initializes a list dp of size 8 (the length of nums), and sets each element to 1. This list will store the length of the longest increasing subsequence that ends at each index.
# It then starts a loop that iterates over each index in nums from right to left. For each index i, it does the following:
# It starts another loop that iterates over each index j to the right of i. For each index j, it checks if nums[i] is less than nums[j]. If it is, it updates dp[i] to be the maximum of dp[i] and 1 + dp[j]. This is because if nums[i] is less than nums[j], we can extend the increasing subsequence that ends at j by nums[i].
# Finally, after filling up the dp list, the function returns the maximum value in dp, which is the length of the longest increasing subsequence in nums.
# Let’s see how this works with the list [10, 9, 2, 5, 3, 7, 101, 18]:

# For the index 7 (the last index), dp[7] is 1 because the longest increasing subsequence that ends at 18 is [18].
# For the index 6, dp[6] is 2 because the longest increasing subsequence that ends at 101 is [18, 101].
# The process continues for the rest of the indices. In the end, dp is [4, 3, 3, 3, 2, 3, 2, 1].
# The maximum value in dp is 4, which is the length of the longest increasing subsequence in the list [10, 9, 2, 5, 3, 7, 101, 18].
# So the function correctly finds that the length of the longest increasing subsequence in the list [10, 9, 2, 5, 3, 7, 101, 18] is 4

# Method 2   Runtime: 51ms
#  the bisect_left function returns the left-most index to insert an element into a sorted list. 
        lst = []
        for num in nums:
            i = bisect_left(lst, num)
            
            if i == len(lst):
                lst.append(num)
            
            else:
                lst[i] = num
        
        return len(lst)
                    
#  It uses a binary search approach to improve the time complexity to O(n log n), where n is the length of nums.

# Here’s how the program works with an example input nums = [10, 9, 2, 5, 3, 7, 101, 18]:

# The function initializes an empty list lst.
# It then starts a loop that iterates over each number in nums. For each number, it does the following:
# It uses the bisect_left function from the bisect module to find the index i in lst where num can be inserted to maintain the sorted order of lst.
# If i is equal to the length of lst, it means that num is greater than all numbers in lst, so it appends num to lst.
# Otherwise, it replaces the number at index i in lst with num. This is because num is smaller than lst[i] and can form a longer increasing subsequence with future numbers.
# Finally, after checking all numbers, it returns the length of lst, which is the length of the longest increasing subsequence in nums.
# Let’s see how this works with the list [10, 9, 2, 5, 3, 7, 101, 18]:

# For the first number 10, lst is empty, so it appends 10 to lst.
# The next number is 9. It can be inserted at index 0 in lst to maintain the sorted order, so it replaces 10 with 9 in lst.
# The process continues for the rest of the numbers. In the end, lst is [2, 3, 7, 18], which is not the longest increasing subsequence itself, but the length of lst is the length of the longest increasing subsequence in the list [10, 9, 2, 5, 3, 7, 101, 18].
# So the function correctly finds that the length of the longest increasing subsequence in the list [10, 9, 2, 5, 3, 7, 101, 18] is 4
