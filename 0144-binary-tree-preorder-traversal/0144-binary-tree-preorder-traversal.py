# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def preorderTraversal(self, root):
        def pre_traversal(root,answer):
            if root is None:
                return
            answer.append(root.val)
            pre_traversal(root.left,answer)
            pre_traversal(root.right,answer)

        answer = []
        pre_traversal(root,answer)
        return answer

       
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna