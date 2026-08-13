# Last updated: 8/13/2026, 8:22:02 PM
class Solution(object):
    def removeDuplicates(self, s):
        stack = []

        for i in s:

            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
        