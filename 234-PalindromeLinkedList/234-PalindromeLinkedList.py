# Last updated: 8/13/2026, 8:24:42 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        if head.next is None:
            return True
        first_head = head
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
           
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        newhead = slow
        current = newhead



        while current:
            nextnode = current.next
            current.next = prev
            prev = current
            current = nextnode
        second_head = prev

        while second_head :
            if second_head.val != first_head.val:
                return False
            second_head = second_head.next
            first_head = first_head.next

        return True

        


            
            