# Last updated: 8/13/2026, 8:25:16 PM
class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[-k: ] + nums[ :-k]
        return nums

        