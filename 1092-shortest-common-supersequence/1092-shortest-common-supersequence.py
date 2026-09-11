class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        
        n = len(str1)
        m = len(str2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        ans = []
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if str1[i] == str2[j]:
                    dp[i][j] = 1+dp[i+1][j+1]
                
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])
        i ,j = 0,0
        while i <n and j<m:
            if str1[i] == str2[j]:
                ans.append(str1[i])
                i+=1
                j += 1
            else:
                if dp[i+1][j]> dp[i][j+1]:
                    ans.append(str1[i])
                    i+=1 
                else:
                    ans.append(str2[j])
                    j+=1
        while j < m:
            ans.append(str2[j])
            j += 1
        while i < n:
            ans.append(str1[i])
            i += 1
        return "".join(ans)

      
                    

                
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna