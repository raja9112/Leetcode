# 19. Remove Nth Node From End of List

# Medium

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
 

# Follow up: Could you do this in one pass?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # #    Two pointer
        # slow = head
        # fast = head

        # # Advance fast to nth position (for the list contains 1 node)
        # for _ in range(n):
        #     fast = fast.next

        # if not fast:
        #     return head.next

        # # Advance slow and fast one by one to get the desired node
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next

        # slow.next = slow.next.next
        # return head


        # Method 2 by adding dummy node
        dummy = ListNode(0, head)
        prev = dummy
        slow, fast = head, head
        for _ in range(n):
            fast = fast.next
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        prev.next = slow.next
        return dummy.next