# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def bst(root,l,h):
            if root is None:
                return True
            if root.val <= l or root.val >= h:
                return False
            left = bst(root.left,l,root.val)
            right = bst(root.right,root.val,h)

            return left and right
        return bst(root,float('-inf'),float('inf'))
            

        

        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna