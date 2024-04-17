# 11. Container With Most Water
 
#  Medium
 
#  You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1

        res = 0
        
        while l <= r:
            area = (r - l) *min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return res

# Here’s how the program would work with this input:

# Initialize two pointers and the result: l is set to 0 (the first index of height), r is set to 8 (the last index of height), and res is set to 0.
# Start a while loop: The loop continues as long as l is less than or equal to r, which means there are still elements to be checked.
# Calculate the area: In the first iteration of the loop, it calculates the area as (8 - 0) * min(1, 7) = 8.
# Update the result: Since 8 is greater than res (0), it updates res to 8.
# Move the pointers: Since height[l] (1) is less than height[r] (7), it increments l by 1.
# Repeat the process: The process is repeated with the updated l and r. In the next iteration, the area is (8 - 1) * min(8, 7) = 56, which is greater than res (8), so it updates res to 56. Since height[l] (8) is not less than height[r] (7), it decrements r by 1.
# Return the maximum area: After the while loop ends, it returns res, which is the maximum area.
# So, for this input, the maxArea method would return 49, indicating that the maximum area of the container that can be formed using the lines represented by height is 49.

# Time complexity: O(n)
# Space complexity: O(1)