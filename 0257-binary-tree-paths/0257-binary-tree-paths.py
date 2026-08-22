# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        self.res = []
        self.curr = []
        def helper(root):
            if root is None:
                return 
            self.curr.append(str(root.val))
            if not root.left and not root.right:
                self.res.append("->".join(self.curr[:]))
                self.curr.pop()
                return
            helper(root.left)
            helper(root.right)
            self.curr.pop()
        
        helper(root)
        return self.res

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna