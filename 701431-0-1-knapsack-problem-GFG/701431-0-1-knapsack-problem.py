class Solution:
    def knapsack(self, W: int, val: list[int], wt: list[int]) -> int:
        
        dp = [[0]* (W+1) for _ in range(len(val)+1)]
        
        for i in range(1,len(val)+1):
            value = val[i-1]
            weight = wt[i-1]
            for w in range(1,W+1):
                if weight <= w:
                    dp[i][w] = max(value+dp[i-1][w-weight],
                                    dp[i-1][w])
                else:
                    dp[i][w] = dp[i-1][w]
                    
        return dp[len(val)][W]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna