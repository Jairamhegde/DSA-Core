# Last updated: 8/13/2026, 8:21:04 PM
class Solution(object):
    def countGoodSubstrings(self, s):
        count = 0

        for i in range(len(s) - 2):
            slices = s[i:i+3]
            if len(set(slices)) == 3:
                count += 1
        return count
           
             
        