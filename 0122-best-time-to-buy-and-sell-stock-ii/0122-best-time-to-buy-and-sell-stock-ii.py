class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        # memo = {}
        # def solve(index,canbuy):
        #     if index == n:
        #         return 0
        #     t = (index,canbuy)
        #     if t in memo:
        #         return memo[t]
        #     if canbuy:
        #         buy = -prices[index] + solve(index+1,False)
        #         hold = solve(index + 1,True)

        #         memo[t] = max(buy,hold)

        #     else:
        #         sell = prices[index] + solve(index + 1,True)
        #         skip = solve(index + 1,False)

        #         memo[t] = max(sell,skip)
        #     return memo[t]
        
        # return solve(0,-1)
    
        dp = [[0]*2 for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            for j in range(1,-1,-1):
                if j == 1:
                    buy = -prices[i] + dp[i+1][0]
                    hold = dp[i+ 1][1]

                    dp[i][j] = max(buy,hold)
                else:
                    sell = prices[i] +dp[i + 1][1]
                    skip = dp[i + 1][0]
                    dp[i][j] = max(sell,skip)

        return dp[0][1]



                 


            




            


       
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna