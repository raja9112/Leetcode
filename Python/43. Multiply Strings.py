# 43. Multiply Strings

# Medium

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"
 

# Constraints:

# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])

                res[i + j] += digit
                res[i + j + 1] += (res[i + j] // 10)  # Place Carry in next position
                res[i+j] = res[i + j] % 10

        res, beg = res[::-1], 0

        while beg < len(res) and res[beg] == 0:
            beg += 1

        res = map(str, res[beg:])
        return "".join(res)

# Initialization: The program first checks if either of the input strings is “0”. If so, it returns “0” as the product of any number and zero is zero. It then initializes a list res of size equal to the sum of the lengths of num1 and num2. This is because the maximum possible length of the product of two numbers is the sum of the lengths of those numbers. The numbers num1 and num2 are reversed for ease of computation.
# Multiplication: The program then enters a nested loop where each digit of num1 is multiplied with each digit of num2. The product, which can be a two-digit number, is added to the appropriate position in res.
# Carry Forward: After the multiplication, if the value at res[i + j] is a two-digit number, the tens place is carried forward to the next position res[i + j + 1]. This is done using the line res[i + j + 1] += res[i + j] // 10. The value at res[i + j] is then updated to be the unit place of the product, using res[i + j] = res[i + j] % 10.
# Removing Leading Zeros: After all the multiplications and carry forwards, res is reversed to get the product in the correct order. However, there may be leading zeros in res. The program uses a while loop to find the position of the first non-zero digit, and removes all the leading zeros.
# Conversion to String: Finally, the digits in res are converted to strings and joined together to form the final product as a string.