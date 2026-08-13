# Last updated: 8/13/2026, 8:28:16 PM
class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1
        return i+1
        