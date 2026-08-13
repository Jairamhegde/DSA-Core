# Last updated: 8/13/2026, 8:21:34 PM
class Solution(object):
    def maxDepth(self, s):
        max_depth = 0
        current_depth = 0
        for i in s:
            if i == "(":
                current_depth += 1
                max_depth = max(current_depth,max_depth)
            elif i == ")":
                current_depth -= 1
        return max_depth