class Solution(object):
    def change(self, amount, coins):
        n = len(coins)
        memo = {}
        def solve(index,current):
            t = (index,current)
            if t in memo:
                return memo[t]
            if index >= n:
                if current == amount:
                    return 1
                return 0
            skip = solve(index+1,current)
            take = 0 
            cur_amt = coins[index]
            if cur_amt + current <= amount:
                take = solve(index,current+ cur_amt)
            total = take+skip
            memo[t] = total
            return total

        return solve(0,0)

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna