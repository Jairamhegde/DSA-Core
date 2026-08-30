class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [0] * (n+1)

        min_cost = 0
        dp[0] = 0
        dp[1] = 0
        for i in range(2,n+1):
            dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])

        return dp[-1]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna