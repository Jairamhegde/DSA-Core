# Last updated: 8/13/2026, 8:22:58 PM
class Solution(object):
    def reverseWords(self, s):
        new = list(s)
        j = 0
        n = len(new)
        for i in range(n):
            if new[i] == " " or  i == n-1:
                l = j
                if i == n-1:
                    r = i
                else:
                    r = i-1
                while l < r:
                    new[l],new[r] = new[r],new[l]
                    l += 1
                    r -= 1
                j = i + 1
        return "".join(new)



            
        