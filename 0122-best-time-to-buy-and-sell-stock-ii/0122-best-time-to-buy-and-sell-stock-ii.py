class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        memo = {}
        def solve(index,canbuy):
            if index == n:
                return 0
            t = (index,canbuy)
            if t in memo:
                return memo[t]
            if canbuy:
                buy = -prices[index] + solve(index+1,False)
                hold = solve(index + 1,True)

                memo[t] = max(buy,hold)

            else:
                sell = prices[index] + solve(index + 1,True)
                skip = solve(index + 1,False)

                memo[t] = max(sell,skip)
            return memo[t]
           


        return solve(0,-1)
                 


            




            


       
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna