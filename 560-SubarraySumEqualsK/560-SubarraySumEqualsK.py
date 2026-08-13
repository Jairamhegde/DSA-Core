# Last updated: 8/13/2026, 8:22:55 PM
class Solution(object):
    def subarraySum(self, nums, k):
        dp = {0:1}
        current_sum = 0
        count = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            required = current_sum - k
            if required in dp:
                count += dp[required]
            
            dp[current_sum] = dp.get(current_sum,0)+1

        return count


        