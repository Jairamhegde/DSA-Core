class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        mod = 10**9+7
        for i in range(1,n+1):
            current = s[i-1]
            if current == "*":
                dp[i] += dp[i-1]*9
            elif current != '0':
                dp[i] += dp[i-1]*1
            
            if i >= 2:
                prev = s[i-2]

                if prev == "*":
                    if current == "*":
                        dp[i] += dp[i-2]*15
                    elif int(current) <= 6 :
                        dp[i] += dp[i-2]*2
                    else:
                        dp[i] += dp[i-2]*1
                elif prev == "1":
                    if current == "*":
                        dp[i] += dp[i-2]*9
                    else:
                        dp[i] += dp[i-2]*1
                elif prev == "2":
                    if current == "*":
                        dp[i] += dp[i-2]*6
                    elif int(current) <= 6:
                        dp[i] += dp[i-2]*1
            dp[i] %= mod
        print(dp)
        return dp[n]
                    
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna