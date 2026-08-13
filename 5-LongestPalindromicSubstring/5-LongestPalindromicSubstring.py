# Last updated: 8/13/2026, 10:20:17 PM
class Solution(object):
    def longestPalindrome(self, s):
        max_length = 0
        new_st = ''
        # if len(s) % 2 ==0:
        for i in range(len(s)):
            l,r = i, i
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                if max_length < r-l+1:
                    max_length = r-l+1
                    new_st = s[l:r+1]
                l -= 1
                r += 1
                        


        else:
             for i in range(len(s)):
                l,r = i, i+1
                while(l >= 0 and r < len(s) and s[l] == s[r]):
                    if max_length < r-l+1:
                        max_length = r-l+1
                        new_st = s[l:r+1]
                    l -= 1
                    r += 1
        return new_st