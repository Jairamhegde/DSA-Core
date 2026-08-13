# Last updated: 8/13/2026, 8:25:52 PM
class Solution(object):
    def findMin(self, nums):
        low = 0
        high = len(nums)-1
        minElement = float('inf')
        while(low <= high):
            mid = (low + high) // 2
            if nums[low] < nums[high]:
                minElement = min(minElement,nums[low])
                break

            if nums[low] <= nums[mid]:
                minElement = min(minElement,nums[low])
                low = mid + 1
            else: 
                minElement = min(minElement,nums[mid])  
                high = mid - 1
        return minElement
            
        