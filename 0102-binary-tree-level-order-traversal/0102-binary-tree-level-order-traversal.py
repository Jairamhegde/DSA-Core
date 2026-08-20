# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    from collections import deque
    def levelOrder(self, root):
        if root is None:
            return []

        queue = deque([root])
        answer = []

        while queue:
            n = len(queue)
            current_level = []

            for _ in range(n):
                item = queue.popleft()
                current_level.append(item.val)
                if item.left is not None:
                    queue.append(item.left)
                    
                if item.right is not None:
                    queue.append(item.right)
            answer.append(current_level)
        return answer
                
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna