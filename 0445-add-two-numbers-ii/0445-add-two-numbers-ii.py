# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        def reversell(head):
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            head = prev
            return head

        h1 = reversell(l1)
        h2 = reversell(l2)
        carry = 0
        newNode = ListNode(0)
        nhead = newNode
        while h1 or h2 or carry > 0:
            add = (h1.val if h1 else 0) + (h2.val if h2 else 0)
            add += carry
            current = add
            if add >= 10:
                n = add
                current = n % 10
                carry = n//10
            else:
                carry = 0
            nn = ListNode(current)
            if newNode.next is None:
                newNode.next = nn
            nhead.next = nn
            nhead = nhead.next
            if h1:
                h1 = h1.next
            if h2:
                h2 = h2.next

        return reversell(newNode.next)

                
        

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna