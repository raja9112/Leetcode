# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.

 

# Example 1:

# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3
# Example 2:

# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
# Example 3:

# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.
 

# Constraints:

# -231 <= n <= 231 - 1


class Solution:
    def isUgly(self, n: int) -> bool:
        prime = [2, 3, 5]

        if n <=0:
            return False

        for i in prime:
            while n%i == 0:
                n = n//i

        return True if n == 1 else False


    #     if n <= 0:  # Handle non-positive numbers
    #         return False

    #     while n > 1:  # Continue dividing until n becomes 1 or irreducible
    #         if n % 2 == 0:
    #             n //= 2
    #         elif n % 3 == 0:
    #             n //= 3
    #         elif n % 5 == 0:
    #             n //= 5
    #         else:
    #             return False  # Not divisible by 2, 3, or 5, not an ugly number

    #     return True  # n has reached 1, it's an ugly number
    