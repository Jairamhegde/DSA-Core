# Last updated: 8/13/2026, 8:23:48 PM
class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return 0
        map = {}
        addfre = False
        total = 0
        for i in range(len(s)):
            map[s[i]] = map.get(s[i],0)+1

        for item in map.values():
            if item % 2 == 0:
                total += item
            else:
                total += item - 1
                addfre = True
        
        return total+1 if addfre == True else total 
            

        