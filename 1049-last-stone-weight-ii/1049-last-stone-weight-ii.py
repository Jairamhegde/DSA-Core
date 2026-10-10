class Solution(object):
    def lastStoneWeightII(self, stones):
        total_sum = sum(stones)
        required = total_sum//2
        n = len(stones)
        dp = [[0]*(required+1) for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,required+1):
                stone = stones[i-1]
                if stone <= j:
                    dp[i][j] = max(stone + dp[i-1][j-stone],dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return total_sum - (2*dp[n][required])

       

            
            


                


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna