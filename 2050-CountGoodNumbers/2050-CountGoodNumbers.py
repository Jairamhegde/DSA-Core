# Last updated: 8/13/2026, 8:21:01 PM
class Solution(object):
    def countGoodNumbers(self, n):
        
        mod = 10**9+7
        even_places = (n + 1)//2
        odd_places = n // 2

        return (pow(5,even_places,mod) * pow(4,odd_places,mod)) % mod
               

       

        