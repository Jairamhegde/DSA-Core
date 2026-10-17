class Solution(object):
    def maxProfit(self, prices):
        n  = len(prices)
        # memo = {}
        # def solve(index,canbuy,tcount):
        #     if index == n :
        #         return 0
        #     if tcount == 2:
        #         return 0
        #     t = (index,canbuy,tcount)
        #     if t in memo:
        #         return memo[t]
        #     if canbuy == 1:
        #         buy = -prices[index] + solve(index+1,0,tcount)
        #         skip = solve(index+1,1,tcount)
        #         max_value =  max(buy,skip)
        #         memo[t]   = max_value
        #         return max_value
        #     else:
        #         sell = prices[index] + solve(index+1,1,tcount+1)
        #         hold = solve(index+1,0,tcount)
        #         max_value =  max(sell,hold)
        #         memo[t]   = max_value
        #         return max_value
        # return solve(0,1,0)
        
        dp=[[[0]*3 for _ in range(2)]for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for k in range(0,2):
                for j in range(0,3):
                    if j > 0:
                        if k == 1:
                            #buy here
                            buy = -prices[i] + dp[i+1][0][j]
                            skip = dp[i+1][1][j]
                            dp[i][k][j] = max(buy,skip)
                        else:
                            #sell here
                            sell = prices[i] + dp[i+1][1][j-1]
                            hold = dp[i+1][0][j]
                            dp[i][k][j] = max(sell,hold)
        return dp[0][1][2]
                    


                    
                        



        




        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna