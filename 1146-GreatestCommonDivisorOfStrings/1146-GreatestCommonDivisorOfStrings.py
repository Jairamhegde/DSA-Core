# Last updated: 8/13/2026, 8:22:01 PM
class Solution(object):

    def gcdOfStrings(self, str1, str2):
        n1 = len(str1)
        n2 = len(str2)

        def gcd(a,b):
            if b <= 0:
                return a
            return gcd(b,a%b)
        if str1 + str2 == str2 + str1:
            gcd = gcd(n1,n2)
            return str2[:gcd]
        else:
            return ""

        