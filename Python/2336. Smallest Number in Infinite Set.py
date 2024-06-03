# 2336. Smallest Number in Infinite Set

# Medium - Leetcode 75

# You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

# Implement the SmallestInfiniteSet class:

# SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
# int popSmallest() Removes and returns the smallest integer contained in the infinite set.
# void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
 

# Example 1:

# Input
# ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
# [[], [2], [], [], [], [1], [], [], []]
# Output
# [null, null, 1, 2, 3, null, 1, 4, 5]

# Explanation
# SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
# smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
# smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
# smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
# smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
#                                    // is the smallest number, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.
 

# Constraints:

# 1 <= num <= 1000
# At most 1000 calls will be made in total to popSmallest and addBack.

class SmallestInfiniteSet:

    def __init__(self):
        self.res = []
        heapify(self.res)
        self.cur = 1

    def popSmallest(self) -> int:
        if len(self.res) != 0:
            return heappop(self.res)
        self.cur += 1
        return self.cur -1

    def addBack(self, num: int) -> None:
        if num not in self.res:    
            if num < self.cur:
                heappush(self.res, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)


# Detailed Explanation
# Initialization:

# self.res is initialized as an empty list which will act as a min-heap.
# self.cur is set to 1.
# popSmallest:

# If self.res is not empty, it pops the smallest element from the heap and returns it.
# If self.res is empty, it returns the value of self.cur and then increments self.cur.
# addBack:

# Adds num back into the set only if num is less than self.cur and not already in self.res.
# Example Flow
# Initial state: self.res = [], self.cur = 1.
# Call popSmallest(): returns 1, now self.cur = 2.
# Call popSmallest(): returns 2, now self.cur = 3.
# Call addBack(2): 2 is added back to self.res because 2 < self.cur (which is 3).
# Call popSmallest(): returns 2 (from the heap), now self.cur remains 3.
# Call popSmallest(): returns 3, now self.cur = 4.


# Using set()
class SmallestInfiniteSet:

    def __init__(self):
        self.res = set()
        # heapify(self.res)
        self.cur = 1

    def popSmallest(self) -> int:
        if len(self.res) != 0:
            # return heappop(self.res)
            res = min(self.res)
            self.res.remove(res)
            return res
        self.cur += 1
        return self.cur -1

    def addBack(self, num: int) -> None:
        if num not in self.res:    
            if num < self.cur:
                # heappush(self.res, num)
                self.res.add(num)
        