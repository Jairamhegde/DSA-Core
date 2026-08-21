# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        def helper(root,diameter):
            if root is None:
                return 0
            left = helper(root.left,diameter)
            right = helper(root.right,diameter)
            total = 1 + left + right
            diameter[-1] = max(diameter[-1],total)
            return  1 +max(left,right)
        
        diameter = [0]
        helper(root,diameter)
        return diameter[0] - 1
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna