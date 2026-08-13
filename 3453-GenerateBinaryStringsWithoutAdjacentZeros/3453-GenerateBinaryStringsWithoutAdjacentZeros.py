# Last updated: 8/13/2026, 8:19:11 PM
class Solution(object):
    def validStrings(self, n):
        array = []
        current = []
        def solve(current):
            if len(current) == n:
                array.append("".join(current))
                return
            current.append("1")
            solve(current)
            current.pop()
            if not current or current[-1] == "1":
                current.append("0")
                solve(current)
                current.pop()
        solve([])
        return array
        