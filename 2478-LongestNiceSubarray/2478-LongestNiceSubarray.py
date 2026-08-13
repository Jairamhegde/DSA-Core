# Last updated: 8/13/2026, 8:20:07 PM
class Solution(object):
    def longestNiceSubarray(self, nums):
        left = 0
        mask = 0
        max_length = 0

        for i in range(len(nums)):
            while mask & nums[i]:
                mask ^= nums[left]
                left += 1
            max_length = max(max_length,i-left + 1)
            mask |= nums[i]
        return max_length
            

        