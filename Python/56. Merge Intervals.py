# 56. Merge Intervals

# Medium

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key= lambda i:i[0])

        res = [intervals[0]]

        for start, end in intervals[1:]:

            lastend = res[-1][1]

            if start <= lastend:
                res[-1][1] = max(lastend, end)
            else:
                res.append([start, end])

        return res

# The merge method takes a list of intervals as input and returns a list of merged intervals. Each interval is a list of two integers [start, end].

# Here’s a brief explanation of the code:

# The function first sorts the intervals in ascending order based on the start time. This is done using the sort method with a lambda function as the key.
# It then initializes the result list res with the first interval.
# The function then iterates over the rest of the intervals. For each interval, it checks if the start time is less than or equal to the end time of the last interval in res. If it is, it means the current interval overlaps with the last interval in res, so it updates the end time of the last interval to be the maximum of the two end times. If it’s not, it means the current interval does not overlap with the last interval in res, so it adds the current interval to res.
# Finally, it returns res, which is the list of merged intervals.
# This solution has a time complexity of O(n log n) due to the sorting operation, where n is the number of intervals. It has a space complexity of O(n)
