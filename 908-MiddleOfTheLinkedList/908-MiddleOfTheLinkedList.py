# Last updated: 8/13/2026, 8:22:18 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        slow = head
        speed = head

        
        while speed and speed.next:
            slow = slow.next
            speed = speed.next.next
            
        return slow
           
      
        