# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Using Array
        # check = []    
        # while head:
        #     check.append(head.val)
        #     head = head.next

        # l, r = 0, len(check) - 1
        # while l <= r:
        #     if check[l] != check[r]:
        #         return False
        #     l += 1
        #     r -= 1
        # return True

        def reverse(node):

            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node

            return prev

        slow = head
        fast = head
        # prev_slow = None  # Keep track of the previous node to the middle node
        while fast and fast.next:
            # prev_slow = slow
            slow = slow.next
            fast = fast.next.next

        # If the number of nodes is odd, move slow one step further
        # if fast:
        #     slow = slow.next

        # Reversing the second half
        reversed_second_half = reverse(slow)  

        # Imagine 2 pointers one is in 1st half and another one is in second half (After middle node)
        while reversed_second_half:
            if head.val != reversed_second_half.val:
                return False
            head = head.next
            reversed_second_half = reversed_second_half.next
        return True