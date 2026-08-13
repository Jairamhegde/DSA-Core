# Last updated: 8/13/2026, 8:28:09 PM
class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        j = 0
        while (j < len(nums)):
            if nums[i] == val and nums[j] != val:
                nums[i],nums[j] = nums[j],nums[i]
            elif nums[i] == val and nums[j] ==val:
                j += 1
            else:
                i += 1
                j += 1
        return i        