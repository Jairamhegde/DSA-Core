# Last updated: 8/13/2026, 10:20:21 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        h1 = l1
        h2 = l2
        prev = None
        new_head = None
        carry = 0
        while h1 or h2 or carry > 0:
            number = (h1.val if h1 else 0 )+( h2.val if h2 else 0)
            number += carry
            n = number
            if number >= 10:
                n = number % 10
                carry = number // 10
            else:
                carry = 0
            new_node = ListNode(n)
            if prev is None:
                prev = new_node
                new_head = prev
            else:
                prev.next = new_node
                prev = new_node
            if h1:
                h1 = h1.next 
            if h2:
                h2 = h2.next 
       
            
        return new_head



        