# 2. Add Two Numbers

# Medium

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            add = v1 + v2 + carry

            carry = add//10
            val = add % 10

            curr.next = ListNode(val)

            # Ptrs
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

# The function initializes a dummy node dummy and a pointer curr that points to the dummy node. It also initializes a variable carry to store the carry from the addition of two digits.
# It then starts a loop that continues as long as there is a node in either l1 or l2 or there is a carry from the previous addition.
# Inside the loop, it does the following:
# It gets the value of the current node of l1 and l2. If a list is already exhausted (i.e., no more nodes), it uses 0 as the value.
# It adds up the two values and the carry to get the sum.
# It updates carry to be the quotient of the sum divided by 10. This is because if the sum is 10 or more, there will be a carry to the next digit.
# It gets the last digit of the sum by taking the remainder of the sum divided by 10. This digit is the value of the new node in the result list.
# It creates a new node with the digit and appends it to the current node pointed by curr.
# It moves the pointer curr to the next node.
# It moves the pointers l1 and l2 to the next node if they are not already None.
# Finally, after the loop, it returns the next node of the dummy node, which is the head of the result list.
# This approach has a time complexity of O(max(n, m)) and a space complexity of O(max(n, m)), where n and m are the lengths of l1 and l2, respectively. This is because in the worst case, we need to iterate through each node in both l1 and l2 and create a new node for each digit in the result.
