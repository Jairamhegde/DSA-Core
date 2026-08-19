# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        ary_length = mountainArr.length()
        low,high = 0,ary_length-1
        peak_index = -1
        peak_ele =0
        while low <= high:
            mid = (low + high )//2
            mid_ele = mountainArr.get(mid)
            right_ele = mountainArr.get(mid + 1)
            if right_ele > mid_ele:
                low = mid + 1
            elif right_ele < mid_ele:
                left_ele = mountainArr.get(mid-1)
                if left_ele < mid_ele:
                    peak_element = mid_ele
                    peak_index = mid
                    break
                else:
                    high = mid -1
        if target > peak_element:
            return -1
        left, right = 0,peak_index

        target_index = -1
        while left <= right:
            mid = (left + right)//2
            mid_ele = mountainArr.get(mid)
            if mid_ele == target :
                target_index = mid
                right = mid -1
            elif mid_ele > target:
                right = mid -1
            else:
                left = mid + 1
        if target_index != -1:
            return target_index
        else:
            left,right = peak_index + 1,ary_length-1
            while left <= right:
                mid = (left + right)//2
                mid_ele = mountainArr.get(mid)
                if mid_ele == target:
                    target_index = mid
                    left = mid + 1
                elif mid_ele > target:
                    left = mid + 1
                else:
                    right = mid - 1
            return target_index


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna