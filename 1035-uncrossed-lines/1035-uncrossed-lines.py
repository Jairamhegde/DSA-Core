class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        for i in range(n1-1,-1,-1):
            for j in range(n2-1,-1,-1):
                if nums1[i] == nums2[j]:
                    dp[i][j] =  1+dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])

        return dp[0][0]


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna