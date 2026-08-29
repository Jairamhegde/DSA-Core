# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        if root is None:
            return 0
        self.max_path = 0
        self.prev = []
        def helper(root):
            if root is None:
                return
            if not self.prev or self.prev[-1] <= root.val:
                self.max_path += 1
            if not self.prev:
                self.prev.append(root.val)
            else:
                self.prev.append(max(self.prev[-1],root.val))
            helper(root.left)
            helper(root.right)

            self.prev.pop()
        helper(root)
        return self.max_path
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna