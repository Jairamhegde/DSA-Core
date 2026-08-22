# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        def helper(root):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return 0
            if root.left and (root.left.left is None  and root.left.right is None):
                v = root.left.val 
            else:
                v = 0
            left = helper(root.left)
            right = helper(root.right)
            return (left + right + v)
        return helper(root)

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna