# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        def solve(root):
            if root is None:
                return [0,0]

            left = solve(root.left)
            right = solve(root.right)

            rob = root.val+left[1] +right[1]

            dontRob = max(left[0],left[1])+max(right[0],right[1])

            return [rob,dontRob]

        return max(solve(root))
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna