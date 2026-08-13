# Last updated: 8/13/2026, 8:24:19 PM
class Solution(object):
    def moveZeroes(self, nums):
        pos = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[pos],nums[i] = nums[i],nums[pos]
                pos += 1
        return nums

        