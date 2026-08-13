# Last updated: 8/13/2026, 10:20:03 PM
class Solution(object):
    def maxArea(self, height):
        max_value = 0
        n = len(height)
        i,j = 0,n-1
        while i < j:
            distance = j - i
            min_val = min(height[i],height[j])
            max_value = max(max_value,(distance*min_val))

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_value