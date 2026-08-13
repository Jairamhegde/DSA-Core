# Last updated: 8/13/2026, 8:24:58 PM
class Solution(object):
    def minSubArrayLen(self, target, nums):
        
        left = 0
        minlen = float('inf')
        currentSum = 0


        for right in range(len(nums)):
            currentSum += nums[right]


            while currentSum >= target:
                minlen = min(minlen,right - left +1)
                currentSum -= nums[left]
                left += 1
        return 0 if minlen == float('inf') else minlen


            