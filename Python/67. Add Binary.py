class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0

    # Pad the binary strings with zeros to make them of equal length
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

    # Iterate from right to left, performing binary addition
        for i in range(max_len -1, -1, -1):
           bit_sum = int(a[i]) + int(b[i]) + carry
           result.append(bit_sum % 2)
           carry = bit_sum // 2
           
    # If there is a carry after the loop, add it to the result
        if carry:
            result.append(carry)
            
    # Reverse the result and join to form the binary sum
        output = ''.join(map(str, result[::-1]))
        return output
    
# Method 2
# Canverting binary value into int, 2 -> base of binary
        # num1 = int(a, 2)
        # num2 = int(b, 2)
        
        # sums = num1 + num2
        
        # Converting int to bin, it will give 0b in front, so removing by[2:]
        # result = bin(sums)[2:]
        # return result
        
# input
# a = 11
# b = 1
# Output = 100