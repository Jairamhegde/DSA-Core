# Last updated: 8/13/2026, 8:26:30 PM
class Solution(object):
    def getRow(self, rowIndex):
        new = []
        new.append(1)
        res = 1
        for i in range(1,rowIndex+1):
            res = res*(rowIndex - i+1)//i
        
            new.append(res)
        
        return new

        