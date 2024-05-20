# 328. Odd Even Linked List

# Medium - Leetcode 75

# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
# Example 2:


# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]
 

# Constraints:

# The number of nodes in the linked list is in the range [0, 104].
# -106 <= Node.val <= 106


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head: return head

        odd = head
        even = head.next
        rhead = even

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = rhead
        return head

# Here’s a step-by-step explanation:

# Initialization: If the head of the linked list is None, the function returns None. Otherwise, it initializes two pointers, odd and even, to the first and second nodes of the list respectively. rhead is a reference to the head of the even-indexed nodes.
# Rearrangement: The code enters a loop that continues as long as there are at least two more nodes in the list. Inside the loop, it updates odd.next to skip one node and even.next to also skip one node. Then it moves the odd and even pointers one step forward along the list.
# Linking Odd and Even Lists: After the loop, all odd-indexed nodes and even-indexed nodes are connected amongst themselves, but the odd list isn’t yet linked to the even list. The code links the end of the odd list to the head of the even list with odd.next = rhead.
# Return Value: Finally, the function returns the head of the rearranged list, which hasn’t changed (it’s still the same as the original head of the list).
# So, if the input list is 1 -> 2 -> 3 -> 4 -> 5, the output of the function will be 1 -> 3 -> 5 -> 2 -> 4.