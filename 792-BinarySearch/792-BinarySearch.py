# Last updated: 8/13/2026, 8:22:24 PM
class Solution(object):
    def search(self, nums, target):
        i = 0
        j = len(nums)-1
        
        while(i <= j):
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                i = mid+1
               
            else :
                j = mid-1
               
        return -1
        
        