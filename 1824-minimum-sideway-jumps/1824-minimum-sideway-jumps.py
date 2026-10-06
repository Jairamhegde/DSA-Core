class Solution(object):
    def minSideJumps(self, obstacles):
        n = len(obstacles)
        dp = [[0]*3 for _ in range(n)]


        for i in range(2,-1,-1):
            if  obstacles[-1] == i+1:
                dp[-1][i] = float('inf')

        for i in range(n-2,-1,-1):
            for j in range(2,-1,-1):
                if obstacles[i] == j+1:
                    dp[i][j] = float('inf')
                else:
                    m = float('inf')
                    for k in range(1,4):
                        if k-1 != j and k != obstacles[i]:
                            m = min(m,
                            1+dp[i+1][k-1])
                    dp[i][j] = min(m,dp[i+1][j])
        return dp[0][1]
                    
                    

            
            

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna