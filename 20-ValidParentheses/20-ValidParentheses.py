# Last updated: 8/13/2026, 8:28:31 PM
class Solution(object):
    def isValid(self, s):
        stack = []
        match = {"]":"[","}":"{",")":"("}
        for i in s:
            if i in {"(","{","["}:
                stack.append(i)
            else:
                if not stack or stack[-1] != match[i]:
                    return False
                else:
                    stack.pop()
        if not stack:
            return True
        else:
            return False
        