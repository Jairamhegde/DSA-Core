class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        prev1 = 1
        prev2 = 0
        for i in range(2,n+1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return prev1

        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna