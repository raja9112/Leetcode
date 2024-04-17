# 919 · Meeting Rooms II

# Medium

# Description
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.)

# Only $39.9 for the "Twitter Comment System Project Practice" within a limited time of 7 days!

# WeChat Notes Twitter for more information（WeChat ID jiuzhangfeifei）


# (0,8),(8,10) is not conflict at 8

# Example
# Example1

# Input: intervals = [(0,30),(5,10),(15,20)]
# Output: 2
# Explanation:
# We need two meeting rooms
# room1: (0,30)
# room2: (5,10),(15,20)
# Example2

# Input: intervals = [(2,7)]
# Output: 1
# Explanation: 
# Only need one meeting room

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here

        start = sorted([i.start for i in range(intervals)])
        end = sorted([i.end for i in range(intervals)])

        res = count = 0
        s = e = 0

        while s < len(intervals):
            if start[s] < end[e]:
                start += 1
                count += 1
            else:
                end += 1
                count -= 1
                res = max(res, count)

        return res
    
intervals = [(0,30),(5,10),(15,20)]
obj = Solution()
obj.min_meeting_rooms(intervals)