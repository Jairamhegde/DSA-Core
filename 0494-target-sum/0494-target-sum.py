class Solution(object):
    def findTargetSumWays(self, nums, target):
        n = len(nums)
        memo = {}
        def solve(index,target,total):
            t = (index,total)
            if t in memo:
                return memo[t]
            if index == n:
                if total == target:
                    return 1 
                return  0
            total += nums[index]
            c2 = solve(index+1,target,total)
            total -= nums[index]
            total -= nums[index]
            c1 = solve(index+1,target,total)
            tt = c1+c2
            memo[t] = tt
            
            return tt
        return solve(0,target,0)
       
            
            
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna