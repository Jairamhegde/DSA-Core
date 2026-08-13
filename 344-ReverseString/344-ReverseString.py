# Last updated: 8/13/2026, 8:24:08 PM
class Solution(object):
    def reverseString(self, s):
        i = 0 
        j = len(s)-1

        while i < j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp

            i += 1
            j -= 1
        return s
        