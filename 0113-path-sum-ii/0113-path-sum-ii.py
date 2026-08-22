# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        self.res = []
        self.current = []
        self.cursum = 0
        def helper(root,targetSum):
            if root is None:
                return 
            self.current.append(root.val)
            if not root.left and not root.right:
                if sum(self.current) == targetSum:
                    self.res.append(self.current[:])
                item = self.current.pop()

                return
            helper(root.left,targetSum)
            helper(root.right,targetSum)

            self.current.pop()
        helper(root,targetSum)
        return self.res
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna