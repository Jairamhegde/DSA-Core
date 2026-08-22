# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def findTilt(self, root):
        self.total = 0
        def helper(root):
            if root is None :
                return 0
            left = helper(root.left)
            right = helper(root.right)
            current = abs(left - right)
            self.total += current
            return left + right + root.val
        helper(root)
        return self.total
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna