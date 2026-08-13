# Last updated: 8/13/2026, 8:27:19 PM
class Solution(object):
    def maxSubArray(self, nums):
        sum = 0
        max_sum = float('-inf')
        for i in range(len(nums)):
            sum += nums[i]
            
            if sum > max_sum:
                max_sum = sum
            if sum < 0:
                sum = 0

            
        return max_sum
        