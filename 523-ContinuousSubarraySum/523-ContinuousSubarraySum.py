# Last updated: 8/13/2026, 8:23:08 PM
class Solution(object):
    def checkSubarraySum(self, nums, k):
        dp = {0:-1}
        current_sum = 0
        n = len(nums)
        for i in range(n):
            current_sum += nums[i]
            rem = current_sum % k
            if rem in dp:
                if (i - dp[rem]) >= 2:
                    return True
            else:
                dp[rem] = i
                
        return False


        