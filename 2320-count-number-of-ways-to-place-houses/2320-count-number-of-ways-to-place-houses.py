class Solution(object):
    def countHousePlacements(self, n):
        mod = 10**9+7
        dp = [0]* (n+1)
        dp[0] = 1
        dp[1] = 2

        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]

        return (dp[-1]**2 )%mod
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna