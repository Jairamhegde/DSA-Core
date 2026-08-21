# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def isBalanced(self, root):
        self.isBal = True
        def height(root):
            if root is None :
                return 0
            left = height(root.left)
            right = height(root.right)
            if abs(left - right) > 1:
                self.isBal = False
            return 1 + max(left,right)
        height(root)
        return self.isBal

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna