# Last updated: 8/13/2026, 8:27:56 PM
class Solution(object):
    def searchRange(self, nums, target):
        i = 0
        j = len(nums)-1
    
        pos2 = -1
        pos1 = -1
        while(i <= j):
            mid = (i + j)//2
            if nums[mid] == target:
                pos2 = mid
                i = mid+1
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        i = 0
        j = len(nums) - 1

        while(i <= j):
            mid =(i + j)//2
            if nums[mid] == target:
                pos1 = mid
                j = mid -1
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return [pos1,pos2]
        