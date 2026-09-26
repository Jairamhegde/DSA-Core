class Solution(object):
    def mostPoints(self, questions):
        n = len(questions)
        memo = {}
        def solve(index):

            if index >= n:
                return 0
            if index in memo:
                return memo[index]
            take = questions[index][0]+solve(index+questions[index][1]+1)

            skip = solve(index+1)
            maxval = max(take,skip)
            memo[index] = maxval
            return maxval

        return solve(0)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna