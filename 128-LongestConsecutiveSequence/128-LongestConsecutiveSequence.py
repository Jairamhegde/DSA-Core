# Last updated: 8/13/2026, 8:26:19 PM
class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
       
        myset = set(nums)
        
        max_consecutives = 1
        for j in myset:
            count = 1
            if j-1 not in myset:
                nexElement = j + 1
                while(nexElement in myset):
                    count += 1
                    nexElement += 1
                    max_consecutives = max(max_consecutives,count)

        return max_consecutives