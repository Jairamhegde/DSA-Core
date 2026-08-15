class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            sum ^=nums[i]
        return sum
        