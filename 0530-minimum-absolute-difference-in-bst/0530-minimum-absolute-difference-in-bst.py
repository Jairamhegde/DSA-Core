# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        self.minval = float('inf')
        self.prev = -1
        def helper(root):
            if root is None:
                return 
            helper(root.left)
            if self.prev == -1:
                self.prev = root.val
            else:
                val = abs(self.prev - root.val)
                self.minval = min(val,self.minval)
                self.prev = root.val
            helper(root.right)
        helper(root)
        return self.minval
           


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna