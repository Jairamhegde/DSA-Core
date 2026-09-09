class Solution(object):
    def longestPalindromeSubseq(self, s):
        s2 = s[::-1]
        n = len(s)
        dp = [[0]*(n+1)for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if s[i] == s2[j]:
                    dp[i][j] = 1+dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])
        return dp[0][0]



                

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna