# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        self.smallest = root.val
        def helper(root):
            if root is None:
                return float('inf')
            if root.val > self.smallest:
                return root.val
            left = helper(root.left)
            right = helper(root.right)
            return min(left,right)
            
        answer= helper(root)
        return -1 if answer == float('inf') else answer




            

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna