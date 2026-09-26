class Solution(object):
    def mostPoints(self, questions):
        n = len(questions)
        dp = [0]* n

        dp[-1] = questions[-1][0]

        for i in range(n-2,-1,-1):
            next_question = i + questions[i][1]+1
            dp[i] = max(
                dp[i+1], 
                questions[i][0]+ (dp[next_question] if next_question < n else 0) )     
        return dp[0]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna