class Solution(object):
    def maxProfit(self, k, prices):
        n  = len(prices)
        memo = {}
        def solve(index,canbuy,tcount):
            if index == n :
                return 0
            if tcount == k:
                return 0
            t = (index,canbuy,tcount)
            if t in memo:
                return memo[t]
            if canbuy == 1:
                buy = -prices[index] + solve(index+1,0,tcount)
                skip = solve(index+1,1,tcount)
                max_value =  max(buy,skip)
                memo[t]   = max_value
                return max_value
            else:
                sell = prices[index] + solve(index+1,1,tcount+1)
                hold = solve(index+1,0,tcount)
                max_value =  max(sell,hold)
                memo[t]   = max_value
                return max_value
        return solve(0,1,0)
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna