# Last updated: 8/13/2026, 8:24:47 PM
class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        count1 = 0
        count2 = 0
        ele1 = None
        ele2 = None
        for i in range(n):
            if nums[i] == ele1:
                count1 += 1
            elif nums[i] == ele2:
                count2 += 1
            elif count1 == 0:
                ele1 = nums[i]
                count1 += 1
            elif count2 == 0:
                ele2 = nums[i]
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        count1 = 0
        count2 = 0
        for j in nums:
            if j == ele1:
                count1 += 1
            if j == ele2:
                count2 += 1
                
        res = []
        mini = n/3
        if count1 > mini:
            res.append(ele1)
        if count2 > mini and ele2 != ele1:
            res.append(ele2)
        return res