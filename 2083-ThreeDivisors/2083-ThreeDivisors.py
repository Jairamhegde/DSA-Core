# Last updated: 8/13/2026, 8:20:40 PM
class Solution(object):
    def isThree(self, n):
        count = 2
        for i in range(n//2,1,-1):
            if n % i == 0:
                count += 1
        if count == 3:
            return True
        else:
            return False
        