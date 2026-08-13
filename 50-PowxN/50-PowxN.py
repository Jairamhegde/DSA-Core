# Last updated: 8/13/2026, 8:27:25 PM
class Solution(object):
    def myPow(self, x, n):
        def findpower(x,n):
            if n == 0:
                return 1
            if n == 1:
                return x
            if n % 2 == 0:
                return findpower(x*x,n//2)
            else:
                return x * findpower(x,n-1)

        if n < 0:
            return 1/findpower(x,-1*n)
        else:
            return findpower(x,n)
        