class Solution(object):
    def findClosestElements(self, arr, k, x):
        n = len(arr)
        l,r = 0,n-k
        while l < r:
            mid = (l+r)//2
            if x-arr[mid] > arr[mid+k] - x:
                l = mid+1
            else:
                r = mid
        return arr[l:l+k]
                
            
        
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna