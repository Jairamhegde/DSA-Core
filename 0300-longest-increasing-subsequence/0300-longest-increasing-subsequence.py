class Solution(object):
    import bisect
    def lengthOfLIS(self, nums):
        tail = []
        n  = len(nums)
        for num in nums:
            pos = bisect.bisect_left(tail,num)
            if pos == len(tail):
                tail.append(num)
            else:
                tail[pos] = num

        return len(tail)

        
        

            
        



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna