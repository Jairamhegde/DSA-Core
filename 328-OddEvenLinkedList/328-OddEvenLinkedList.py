# Last updated: 8/13/2026, 8:24:11 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next :
            return head
        oddind = head
        evenind = head.next
        even = head.next
        

        while evenind and evenind.next:
            oddind.next = oddind.next.next
            oddind = oddind.next

            evenind.next = evenind.next.next
            evenind = evenind.next
        oddind.next = even

        
        return head

        