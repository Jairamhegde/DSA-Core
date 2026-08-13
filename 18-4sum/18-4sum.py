# Last updated: 8/13/2026, 8:28:56 PM
class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        print(nums)
        n = len(nums)
        new = []
        for i in range(n):
            if i > 0 and  nums[i] == nums[i-1]:
                 continue
            for j in range(i+1,n):
                if j > i+1 and nums[j] == nums[j-1]:
                     continue
                     
                left = j + 1
                right = n-1
                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum == target:
                        new.append([nums[i] , nums[j] , nums[left] , nums[right]])
                        while left < right and  nums[left] == nums[left+1]:
                            left += 1
                        while right > left  and  nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif target > sum :
                        left += 1
                    else:
                        right -= 1 
        return new