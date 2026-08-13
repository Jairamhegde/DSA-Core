# Last updated: 8/13/2026, 8:22:09 PM
class Solution(object):
    def removeOuterParentheses(self, s):
        count = 0
        new = ""
        i = 0
        for j in range(len(s)):

            if s[j] == "(":
                count += 1
            elif s[j] == ")":
                count -= 1
            if count == 0:
                new += s[i+1:j]
                i = j+1
        return new
        