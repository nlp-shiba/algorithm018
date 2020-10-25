# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        merged = ListNode()
        start = merged
        while l1 and l2:
            if l1.val < l2.val:
                merged.next = l1
                merged = merged.next
                l1 = l1.next
            else:
                merged.next = l2
                merged = merged.next
                l2 = l2.next
        if l1:
            merged.next = l1
        else:
            merged.next = l2
        return start.next