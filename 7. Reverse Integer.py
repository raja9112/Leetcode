# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -231 <= x <= 231 - 1


import math
class Solution:
    def reverse(self, x: int) -> int:
        
        min =-2147483648
        max = 2147483647

        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            if (res > max // 10 or (res == max // 10 and digit >= max % 10)):
                return 0
            if (res < min // 10 or (res == min // 10 and digit <= min % 10)):
                return 0
            res = (res * 10) + digit

        return res
    
    
    