# Last updated: 8/13/2026, 8:21:26 PM
class Solution(object):
    def maximumUniqueSubarray(self, nums):
        from collections import defaultdict
        max_score = 0
        cur_sum = 0
        dp = defaultdict(int)
        left = 0
        for right in range(len(nums)):
            cur_sum += nums[right]
            dp[nums[right]] += 1
            while dp[nums[right]] > 1:
                cur_sum -= nums[left]
                dp[nums[left]] -= 1
                left += 1
            max_score= max(max_score, cur_sum)
        return max_score



       