# Last updated: 8/13/2026, 8:24:26 PM
class Solution(object):
    def isAnagram(self, s, t):
        ar = [0]*26
        if len(s) != len(t):
            return False
        for i in s:
            ar[ord(i)-97] += 1
        for j in t:
            ar[ord(j)-97] -= 1
        for m in ar:
            if m != 0:
                return False
        return True
        
            
            # d2[j]=d2.get(j,0)+1
            
        # for k in (s+t):
        #     if(d1.get(k,0)!=d2.get(k,0)):
        #         return False
        # return True
        