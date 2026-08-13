# Last updated: 8/13/2026, 8:21:06 PM
class Solution(object):
    def maxFrequency(self, nums, k):
        nums.sort()
        n = len(nums)
        cur_sum = 0
        max_len = 0
        left = 0
        for i in range(n):
            cur_sum += nums[i]
            while (nums[i]*(i-left+1)) > cur_sum + k:
                cur_sum -= nums[left]
                left += 1
            max_len = max(max_len,i-left + 1)
            
        return max_len
            
        