# Last updated: 8/13/2026, 8:28:04 PM
class Solution(object):
    def strStr(self, haystack, needle):
        n = len(needle)
        i = 0
        j = n
        le = len(haystack)
        while(j <= le):
            if haystack[i:j] == needle:
                return i
            j += 1
            i += 1
        return -1
        