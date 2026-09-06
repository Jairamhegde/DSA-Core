class Solution(object):
    def findNumberOfLIS(self, nums):
        n = len(nums)
        count = 0
        dp = [1]*n
        dpc = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    val = dp[j]
                    if (val+1) > dp[i]:
                        dpc[i] = dpc[j]
                        dp[i] = val + 1
                    elif (val + 1) == dp[i]:  
                        dpc[i] += dpc[j] 
        print(dp)
        print(dpc)
        maxlength = max(dp)
        return sum(dpc[k] for k in range(n) if dp[k]== maxlength)

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna