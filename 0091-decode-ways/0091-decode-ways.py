class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        dp=[0]*(n+1)
        dp[0] = 1
        if not dp:
            return 0
        if s[0] != "0":
            dp[1] = 1
       
        for i in range(2,n+1):
            sumation = 0
            first = int(s[i-1])
            total = int(s[i-2]) * 10 + first
            if first != 0:
                sumation += dp[i-1]
            if total >= 10 and total <= 26:
                sumation += dp[i-2]
            dp[i] = sumation
        return dp[-1]

       

        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna