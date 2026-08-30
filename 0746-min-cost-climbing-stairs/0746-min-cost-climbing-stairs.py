class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        prev2 = 0
        prev1 = 0
        for i in range(2,n+1):
            current = min((prev1+ cost[i-1]),(prev2+cost[i-2]))
            prev2 = prev1
            prev1 = current
        return prev1
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna