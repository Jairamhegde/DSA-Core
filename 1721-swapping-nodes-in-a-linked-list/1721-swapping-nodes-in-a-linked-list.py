# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        second_node = length - k + 1
        prev_node = ListNode()

        prev_node.next = head
        def find_node(k):
            current = head
            l = 0
            prev = prev_node
            prev.next = head
            while current:
                l += 1
                if l == k:
                    return prev,current
                current = current.next
                prev = prev.next
            return None,None
       

        prev,cur=find_node(k)
        prev2,cur2 = find_node(second_node)

        prev.next, prev2.next = cur2,cur
        cur.next,cur2.next = cur2.next,cur.next
    

        return prev_node.next





        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna