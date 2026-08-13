# Last updated: 8/13/2026, 8:28:27 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)

        prev = dummy
        head = list1 
        tail = list2 
     
        while head and tail:
            if head.val <= tail.val:
                prev.next = head
                prev = head
                head = head.next
            else:
                prev.next = tail
                prev = tail
                tail = tail.next
        if tail:
            prev.next = tail
        if head:
            prev.next = head
        return dummy.next
        