# Given the head of a singly linked list, reverse the list, and return the reversed list.

# EASY - Leetcode 75

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative approach
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

        # Recursion 
        # def reverse(cur, prev):
        #     if cur is None:
        #         return prev
        #     else:
        #         next_node = cur.next
        #         cur.next = prev
        #         return reverse(next_node, cur)
        # return reverse(head, None)
        
        
        