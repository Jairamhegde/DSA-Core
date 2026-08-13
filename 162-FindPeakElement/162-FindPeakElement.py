# Last updated: 8/13/2026, 8:25:44 PM
class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) //2
            if (mid ==  0 or nums[mid-1] < nums[mid]) and (mid == n-1 or nums[mid] > nums[mid+1]):
                return mid
            if nums[mid+1] >= nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return 0
        
        