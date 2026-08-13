# Last updated: 8/13/2026, 8:28:01 PM
class Solution(object):
    def nextPermutation(self, nums):
        if not nums:
            return []
        def reverse(arr,left,right):
            l = left
            r = right
            while l < r:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
                r -= 1

        n = len(nums)
        pivot = -1
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                pivot = i
                break
        if pivot == -1:
            reverse(nums,0,n-1)
        else:
            index = -1
            minval = float('inf')
            for j in range(n-1,pivot,-1):
                element = nums[j]
                if element > nums[pivot]:
                    if element < minval:
                        index = j
                        minval = element
            nums[pivot],nums[index] = nums[index],nums[pivot]
            reverse(nums,pivot+1,n-1)
        return nums