# Last updated: 8/13/2026, 8:23:46 PM
class Solution(object):
    def thirdMax(self, nums):
        

        first_max= float('-inf')
        second_max = float('-inf')
        third_max = float('-inf')
        for i in range(len(nums)):
            if nums[i] > first_max:
                first_max = nums[i]
        for i in range(len(nums)):
            if nums[i] > second_max and nums[i] != first_max:
                second_max = nums[i]
        for i in range(len(nums)):
            if nums[i] > third_max:
                if nums[i] != second_max and nums[i] != first_max:
                    third_max = nums[i]
        if third_max != float('-inf'):
            return third_max
        return first_max
        

        