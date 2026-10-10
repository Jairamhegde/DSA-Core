class Solution(object):
    from collections import Counter
    def findMaxForm(self, strs, m, n):
        k = len(strs)
        dp = [[[0]*(n+1) for _ in range(m+1)]for _ in range(k+1)]

        for i in range(k-1,-1,-1):
            zeros = strs[i].count("0")
            ones = strs[i].count("1")
            for j in range(m+1):
                for l in range(n+1):
                    skip =dp[i+1][j][l]
                    
                    take = 0
                    if zeros <= j and ones <= l:
                        take = 1 + dp[i+1][j-zeros][l-ones]

                    dp[i][j][l] = max(take,skip)
        return dp[0][m][n]




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna