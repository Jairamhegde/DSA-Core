# Last updated: 8/13/2026, 10:20:24 PM
class Solution(object):
    def twoSum(self, nums, target):
        map = {}

        for i in range(len(nums)):

            required = target - nums[i]
            if required in map:
                return [map[required],i]
            if not nums[i] in map:
                map[nums[i]] = i
        return []

        
                

        