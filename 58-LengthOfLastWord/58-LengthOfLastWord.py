# Last updated: 8/13/2026, 8:27:13 PM
class Solution(object):
    def lengthOfLastWord(self, s):
        length = 0
       
        i = len(s)-1
        while i > 0 and s[i] == ' ':
            i -= 1
        if i < 0:
            return 0
        for i in range(i,-1,-1):
            if s[i] == " ":
                return length
            length += 1
        return length

        