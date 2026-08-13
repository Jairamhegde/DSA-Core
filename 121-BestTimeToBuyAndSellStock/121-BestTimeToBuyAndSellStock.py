# Last updated: 8/13/2026, 8:26:26 PM
class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        min = float("inf")
        for i in prices:
            if i < min:
                min = i
            else:
                max_profit = max(max_profit,i-min)
        return max_profit
        


        