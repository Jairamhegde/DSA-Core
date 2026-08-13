# Last updated: 8/13/2026, 8:20:17 PM
class Solution(object):
    def rearrangeArray(self, nums):
        new = [0]*len(nums)
        possitive_idx=0
        negetive_idx = 1
        for i in range(len(nums)):
            if nums[i] < 0:
                new[negetive_idx] = nums[i]
                negetive_idx += 2
            else:
                new[possitive_idx] = nums[i]
                possitive_idx += 2
        

    
        return new