# Last updated: 8/13/2026, 8:23:17 PM
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maximum = 0
        sum = 0
        for j in range(len(nums)):
            if nums[j] == 1:
                sum += 1
                if sum > maximum:
                    maximum = sum
            else:
                sum = 0
        return maximum

        