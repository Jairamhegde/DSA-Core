class Solution(object):
    def minDistance(self, word1, word2):
        n = len(word1)
        m = len(word2)
        dp = [[0]*(m+1)for _ in range(n+1)]
        for i in range(1,n+1):
            dp[i][0] = i 
        for i in range(1,m+1):
            dp[0][i] = i

        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] 
                else:
                    dp[i][j] =1+ min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
        return dp[n][m]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna