# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        def helper(root):
            
            if root is None:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            total = 1 + left + right
            self.diameter = max(self.diameter,total)
            return  1 +max(left,right)
        
        
        helper(root)
        return self.diameter -1
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna