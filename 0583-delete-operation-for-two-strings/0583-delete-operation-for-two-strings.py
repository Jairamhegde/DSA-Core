class Solution(object):
    def minDistance(self, word1, word2):
        n = len(word1)
        m = len(word2)
        dp = [[0]*(m+1)for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if word1[i] == word2[j]:
                    dp[i][j] = 1+ dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1],dp[i+1][j])
        return (m- dp[0][0])+ (n-dp[0][0])
       
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna