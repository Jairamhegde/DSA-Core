# Last updated: 8/13/2026, 8:21:20 PM
class Solution(object):
    def check(self, nums):

        if len(nums) == 1:
            return True
        inverstioncount = 0
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                inverstioncount += 1
                if inverstioncount > 1:
                    return False
        if nums[0] < nums[-1]:
            inverstioncount += 1
        return inverstioncount <= 1