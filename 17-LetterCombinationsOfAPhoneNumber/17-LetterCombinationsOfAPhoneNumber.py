# Last updated: 8/13/2026, 8:29:02 PM
class Solution(object):
    def letterCombinations(self, digits):
        d = {
            "0":"",
            "1":"",
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        def helper(new,current,index):
            if len(current) == len(digits):
                new.append("".join(current))
                return
                
            s = d[digits[index]]
            for i in s:
                current.append(i)
                helper(new,current,index+1)
                current.pop()
        new = []
        if digits:
            helper(new,[],0)
        return new
