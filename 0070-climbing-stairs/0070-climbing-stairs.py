class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        dp = [0]*(n+1)

        dp[1] = 1
        dp[2] = 2
        total_ways = 0

        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna