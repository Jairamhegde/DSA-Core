class Solution(object):
    def maximumSubarraySum(self, nums, k):
        hmap = {}
        cursum  = 0
        maxsum = float('-inf')
        maxlen = -1
        for i in range(len(nums)):
            cursum += nums[i]
            needed1 = nums[i] - k
            needed2 = nums[i] + k
            if needed1 in hmap:
             
                maxsum =max(maxsum ,cursum - hmap[needed1]+needed1)  
            if needed2 in hmap:
                
                maxsum = max(maxsum,cursum - hmap[needed2] +needed2) 
            if nums[i] in hmap:
                hmap[nums[i]] = min(hmap[nums[i]],cursum)
            else:hmap[nums[i]] = cursum
        return maxsum if maxsum != float('-inf') else 0





        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna