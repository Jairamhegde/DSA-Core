# Last updated: 8/13/2026, 8:23:59 PM
class Solution(object):
    def firstUniqChar(self, s):
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        for j in s:
              if d.get(j)==1:
                    return s.index(j)
        return -1
        