# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        self.res = []
        self.cur = []
        def helper(root):
            if root is None :
                return 
            self.cur.append(str(root.val))
            if root.left is None and root.right is None:
                self.res.append(int("".join(self.cur)))
                self.cur.pop()
                return

            helper(root.left)
            helper(root.right)
            
            self.cur.pop()

        helper(root)
        return sum(self.res)
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna