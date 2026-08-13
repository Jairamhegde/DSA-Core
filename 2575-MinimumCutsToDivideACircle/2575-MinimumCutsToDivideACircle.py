# Last updated: 8/13/2026, 8:19:35 PM
class Solution(object):
    def numberOfCuts(self, n):
        if n == 1:
            return 0
        return n // 2 if n % 2 == 0 else n
        