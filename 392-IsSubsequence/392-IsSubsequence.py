# Last updated: 8/13/2026, 8:23:54 PM
class Solution(object):
    def isSubsequence(self, s, t):
        i = j = 0

        for j in range(len(t)):
            if i >= len(s):
                break
            if t[j] == s[i]:
                i += 1
        if i >= len(s):
            return  True
        else:
            return False
        





        