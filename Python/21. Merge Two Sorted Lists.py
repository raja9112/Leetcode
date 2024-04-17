# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = dummy = ListNode()

        # while l1 and l2:  Time exceeded
        #   if l1.val < l2.val:
        #      current.next = l1
        #      l1 = l1.next
        #   else:
        #      current.next = l2
        #      l2 = l2.next
        #   current = current.next
        
        #  One possible optimization is to avoid updating the current node 
        # for every comparison and instead directly link the next node in the merged list.
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next, list1 = list1, list1.next
            else:
                current.next, list2 = list2, list2.next
            current = current.next

        current.next = list1 or list2
        
        return dummy.next
    
# Initialization:

# dummy is initialized as an empty node.
# current is set to dummy.
# Iterating through the Lists:

# The while loop starts since both l1 and l2 are not empty.
# Comparing Values:

# At the first iteration, l1.val (1) is equal to l2.val (1). Since they are equal, it doesn't matter which one is chosen. Let's say l1 is chosen.
# current.next is set to l1 (1).
# l1 is moved to its next node (l1 = l1.next).
# current is moved to the next node (current = current.next).
# At the second iteration, l1.val (2) is less than l2.val (3).
# current.next is set to l1 (2).
# l1 is moved to its next node (l1 = l1.next).
# current is moved to the next node (current = current.next).
# At the third iteration, l1.val (4) is greater than l2.val (3).
# current.next is set to l2 (3).
# l2 is moved to its next node (l2 = l2.next).
# current is moved to the next node (current = current.next).
# Appending Remaining Nodes:

# After the loop, l1 is exhausted, but l2 still has one more node (4). This node is directly appended to the merged list.
# current.next is set to l2 (4).
# Returning the Merged List:

# The function returns the head of the merged list, excluding the dummy node (dummy.next).
# Final Merged List:

# The final merged list is [1, 1, 2, 3, 4, 4].