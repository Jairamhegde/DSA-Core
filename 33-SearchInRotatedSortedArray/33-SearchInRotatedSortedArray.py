# Last updated: 8/13/2026, 8:27:57 PM
class Solution(object):
    def search(self, nums, target):
        i = 0
        j = len(nums) - 1
        while (i <= j):
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[i] <= nums[mid]:
                if nums[i] <= target <= nums[mid]:
                    j = mid-1
                else:
                    i = mid +1
            else:
                if nums[mid] <= target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
        return -1 
        

        