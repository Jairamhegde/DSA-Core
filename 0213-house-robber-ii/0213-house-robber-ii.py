class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        prev1 = 0
        prev2 = 0

        for i in range(1,len(nums)):
            current = max(nums[i] + prev2,prev1)
            prev2 = prev1
            prev1 = current
        prev11 = 0
        prev22 = 0
        for j in range(len(nums)-1):
            current = max(nums[j] + prev22,prev11)
            prev22 = prev11
            prev11 = current

        return max(prev11,prev1)
        

        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna