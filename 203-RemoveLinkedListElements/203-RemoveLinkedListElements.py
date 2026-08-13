# Last updated: 8/13/2026, 8:25:09 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        current = head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while current :
            if current.val == val:
                prev.next = current.next
                
            else:
                prev = current
            current = current.next
        return dummy.next
        