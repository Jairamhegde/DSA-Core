# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    current_sum = 0
    def hasPathSum(self, root, targetSum):
        
            if root is None:
                return False
            targetSum -= root.val
            if root.left is None and root.right is None:
                return targetSum == 0
            return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)

        

        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna