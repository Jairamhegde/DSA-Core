class Solution(object):
    from collections import Counter
    def deleteAndEarn(self, nums):
        c = Counter(nums)
        nums = sorted(list(set(nums)))
        prev = 0
        prev2 = 0
        maxpoint = nums[-1]
        for i in range(len(nums)):
            current = nums[i]* c[nums[i]]
            if i>0 and nums[i] == (nums[i-1]+1):
                currentEarn=max(prev2+current,prev)
            else:
                currentEarn = prev + current
            prev2 , prev  = prev,currentEarn
        return prev



       

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna