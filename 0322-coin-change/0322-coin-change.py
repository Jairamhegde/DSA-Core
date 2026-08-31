class Solution(object):
    def coinChange(self, coins, amount):
        memo = {}
        def solve(index,ammount):
            if (index,ammount) in memo:
                return memo[(index,ammount)]
            if ammount == 0:
                return 0
            if index == len(coins):
                return float('inf')

            take = float('inf')
            if ammount >= coins[index]:
                take = 1+solve(index,ammount - coins[index])

            skip = solve(index+1,ammount)
            min_val = min(skip,take)
            if (index,ammount) not in memo:
                memo[(index,ammount)] = min_val
            return min(skip,take)
        res = solve(0,amount)
        return res if res != float('inf') else -1     

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna