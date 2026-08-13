# Last updated: 8/13/2026, 8:28:23 PM
class Solution(object):
    def generateParenthesis(self, n):
        array = []
        res=[]
        def solve(openCount,closeCount):
            if openCount == closeCount == n:
                array.append("".join(res))
                return
            if openCount < n:
                res.append("(")
                solve(openCount+1,closeCount)
                res.pop()
            if closeCount < openCount:
                res.append(")")
                solve(openCount,closeCount+1)
                res.pop()
        solve(0,0)
        return array
        