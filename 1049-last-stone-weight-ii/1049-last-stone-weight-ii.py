class Solution(object):
    def lastStoneWeightII(self, stones):
        total_sum = sum(stones)
        required = total_sum//2
        
        n = len(stones)
        memo = {}
        self.maxsum = float('-inf')
        def solve(index,cursum):
            t = (index,cursum)
            if t in memo:
                return memo[t]
            if index == n:
                self.maxsum = max(self.maxsum,cursum)if cursum <= required else self.maxsum
                return 0
            take = 0
            current = stones[index]
            if current + cursum <= required:
                take = current + solve(index+1,cursum + current)
            skip = solve(index+1,cursum)

            memo[t] = max(skip ,take)
            return max(skip ,take)
           

        solve(0,0)
        return total_sum - 2*self.maxsum

       

            
            


                


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna