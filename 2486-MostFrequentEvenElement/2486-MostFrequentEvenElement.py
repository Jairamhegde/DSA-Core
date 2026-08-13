# Last updated: 8/13/2026, 8:20:00 PM
class Solution(object):
    def mostFrequentEven(self, nums):
        map = {}
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                map[nums[i]] = map.get(nums[i],0)+1
        max_ele = -1
        max_count = 0
        for key,value in map.items():
            if value > max_count:
                max_count = value
                max_ele = key
            elif value == max_count:
                max_ele = min(max_ele,key)

        return max_ele

        
                


            
        