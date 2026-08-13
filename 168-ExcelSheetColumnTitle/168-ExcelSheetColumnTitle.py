# Last updated: 8/13/2026, 8:25:38 PM
class Solution(object):
    def convertToTitle(self, columnNumber):
        n = columnNumber
        res = ""
        while n > 0:
            rem = (n - 1) % 26
            val = ord("A") + rem
            charector = chr(val)
            res = charector + res
            n = (n-1) // 26
        return res

        