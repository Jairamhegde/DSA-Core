# Last updated: 8/13/2026, 8:28:38 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        
        if not head :
            return head
        current = head
        length = 0
        while current:
            length += 1
            current = current.next

        node = length - n
        print(node)
        idx = 0
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        newcurrent = head
        while newcurrent and idx != node:
           prev = newcurrent
           newcurrent = newcurrent.next
           idx += 1
        if newcurrent is None:
            return head
        prev.next = newcurrent.next
        return dummy.next
        
        