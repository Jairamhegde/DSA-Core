class Solution(object):
    def tribonacci(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 1
        elif n == 0:
            return 0

        prev1 = 1
        prev2 = 1
        prev3 = 0
        for i in range(3,n+1):
            current= prev1 + prev2 + prev3
            prev3 = prev2
            prev2 = prev1
            prev1 = current
        return prev1
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna