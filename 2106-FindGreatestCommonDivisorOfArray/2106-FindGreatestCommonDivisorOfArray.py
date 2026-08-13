# Last updated: 8/13/2026, 8:20:37 PM
class Solution(object):
    def findGCD(self, nums):
        max_ele = max(nums)
        min_ele = min(nums)
        def gcd(a,b):
            if b <= 0 :
                return a
            return gcd(b,a% b)
        return gcd(max_ele,min_ele)

        