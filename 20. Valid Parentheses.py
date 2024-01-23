class Solution:
    def isValid(self, s: str) -> bool:
        map = {")":"(", "}":"{", "]":"["}
        stack = []
        for i in s:
            if i not in map:
                # If the element is opening bracket, append it to stack
                stack.append(i)
                continue
            if not stack or stack[-1] != map[i]:
            # Checks if the stack is empty or top element of stack is equal to the map[i]
            # map[i] return vlue of key.
                return False
            stack.pop()     # If it meets, pop top element from stack
        return not stack    # After iterating all elements of input stack will become empty and return True
    
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.