class Solution(object):
    def findClosestElements(self, arr, k, x):
        left = 0
        n = len(arr)
        for i in range(n):
            while (i - left + 1) > k:
                left += 1
            if (i - left + 1) == k:
                if i == n-1 or  (x-arr[left]) <= (arr[i+1]-x):
                    return arr[left:i+1]
        return []
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna