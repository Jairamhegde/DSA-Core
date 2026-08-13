# Last updated: 8/13/2026, 8:25:25 PM
class Solution(object):
    def majorityElement(self, nums):
        element = nums[0]
        current_count = 0
        max_count = 0
        n = len(nums)
        for i in range(len(nums)):
            if current_count == 0:
                element = nums[i]
                count = 0
            if nums[i] == element:
                current_count += 1
                if current_count > max_count and current_count >  (n/2):
                    max_count = max(current_count,max_count)
            else:
                current_count -= 1

        return element
           
        