# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        self.summap = {0:1}
        self.path = 0
        self.cursum = 0
        def helper(root,targetSum):
            if root is None :
                return
            self.cursum += root.val
            needed = self.cursum - targetSum
            if needed in self.summap:
                self.path += self.summap[needed]
            self.summap[self.cursum] = self.summap.get(self.cursum,0) + 1 
            helper(root.left,targetSum)
            helper(root.right,targetSum)
            self.summap[self.cursum] = self.summap.get(self.cursum) - 1
            self.cursum -= root.val
            
        helper(root,targetSum)
        return self.path

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna