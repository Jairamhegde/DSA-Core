# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        self.maxsum = float('-inf')
        def solve(root):
            if root is None:
                return 0
            left =solve(root.left)
            right =solve(root.right)
            value = root.val
            self.maxsum = max(self.maxsum,value,value+left,value+right,value+left+right)
            return max(value,value+ max(left,right))

        solve(root)
        return self.maxsum


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna