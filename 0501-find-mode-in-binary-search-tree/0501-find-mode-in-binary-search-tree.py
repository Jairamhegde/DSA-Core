# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        self.prev = root.val
        self.count = 0
        self.answer = []
        self.max_count = 0
        def helper(root):
            if root is None:
                return
            helper(root.left)
            if self.count == 0:
                self.prev = root.val
            
            if self.prev != root.val:
                self.prev = root.val
                self.count = 0
            if self.prev == root.val:
                self.count += 1

                if self.max_count < self.count:
                    self.answer = [root.val]
                    self.max_count = self.count
                elif self.max_count == self.count:
                    self.answer.append(root.val)
            
            helper(root.right)
        helper(root)
        return self.answer

            


            


        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna