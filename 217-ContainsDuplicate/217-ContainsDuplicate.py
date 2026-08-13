# Last updated: 8/13/2026, 8:24:54 PM
class Solution(object):
    def containsDuplicate(self, nums):
        hl=[0]*10
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1

        # for j in nums:
        #     d[j]=hl[j]
        for k in d.values():
            if(k>1):
                return True
        return False
        