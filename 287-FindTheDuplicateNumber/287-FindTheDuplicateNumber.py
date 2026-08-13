# Last updated: 8/13/2026, 8:24:14 PM
class Solution(object):
    def findDuplicate(self, nums):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
                 
        return 0
            
        