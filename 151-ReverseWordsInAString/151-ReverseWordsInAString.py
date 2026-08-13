# Last updated: 8/13/2026, 8:25:58 PM
class Solution(object):
    def reverseWords(self, s):
        new = s.split()
        new.reverse()
        return " ".join(new).strip()