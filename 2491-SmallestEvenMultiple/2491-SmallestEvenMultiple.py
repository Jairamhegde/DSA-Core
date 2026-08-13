# Last updated: 8/13/2026, 8:19:43 PM
class Solution(object):
    def smallestEvenMultiple(self, n):
        for i in range(n,(n*100)+1,n):
            if i % 2 == 0:
                return i
                
        