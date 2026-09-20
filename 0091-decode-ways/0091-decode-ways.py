class Solution(object):
    def numDecodings(self, s):
        memo = {}
        n = len(s)
        def solve(s,index):
            if index in memo:
                return memo[index]
            if index >= n:
                return 1
            if s[index] == "0":
                return 0
            
            take1 = solve(s,index+1)
            take2 = 0
            if index < n-1:
                val =  int(s[index:index+2])
                if val >= 10 and val <= 26:
                    take2 = solve(s,index +2)
            total = take1 + take2
            memo[index] = total
            return total
        return solve(s,0)

        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna