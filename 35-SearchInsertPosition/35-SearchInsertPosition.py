# Last updated: 8/13/2026, 8:27:52 PM
class Solution(object):
    def searchInsert(self, nums, target):
        i = 0
        j = len(nums)-1
        ans = len(nums)
        while(i <= j):
            mid = (i + j)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                ans = mid
                j = mid - 1
            else:
                i = mid + 1

        return ans
        