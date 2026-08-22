# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    
    def kthSmallest(self, root, k):
     
        self.kth = 0
       
        def helper(root,k):
            if root is None:
                return 
            left = helper(root.left,k)
            if left is not None:
                return left
            self.kth += 1
            if self.kth == k:
                return root.val
            
            
            return helper(root.right,k)

        
        return helper(root,k)


        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna