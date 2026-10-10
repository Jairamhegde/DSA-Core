class Solution(object):
    def change(self, amount, coins):
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1,n+1):
            coin = coins[i-1]
            for j in range(1,amount+1):
                skip = dp[i-1][j]

                take = 0
                if coin <= j:
                    take = dp[i][j-coin]

                dp[i][j] = skip+take  

        return dp[n][amount]              

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna