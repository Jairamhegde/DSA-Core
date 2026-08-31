class Solution(object):
    def coinChange(self, coins, amount):
        dp = [float('inf')]*(amount + 1)
        dp[0] = 0

        for i in range(1,amount+1):
            for k in coins:
                if k <= i:
                    dp[i] = min(dp[i],
                    1 + dp[i - k]
                    ) 
        val = dp[amount]
        return val if val != float('inf') else -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna