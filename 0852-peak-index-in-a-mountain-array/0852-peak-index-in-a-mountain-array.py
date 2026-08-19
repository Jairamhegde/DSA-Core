class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low ,high = 0,len(arr)-1
        while low <= high:
            mid = (low + high)//2
            mid_ele = arr[mid]
            right_ele = arr[mid+1]
            if right_ele > mid_ele:
                low = mid + 1
            else:
                left_ele = arr[mid-1]
                if left_ele < mid_ele:
                    return mid
                else:
                    high = mid -1
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna