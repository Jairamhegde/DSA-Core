class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        n1 = len(nums1)
        n2 = len(nums2)
        total_length = (n1 + n2)
        left_length =  (n1 + n2 +1)//2

        low,high = 0,n1
        while low <= high:
            mid = (low + high)//2
            l1  = nums1[mid-1] if mid > 0 else float('-inf')
            r1 = nums1[mid] if mid < n1 else float('inf')
            j = left_length -mid
            l2  = nums2[j-1] if j > 0 else float('-inf')
            r2 = nums2[j] if j < n2 else float('inf')

            if l1 <= r2 and l2 <= r1:
                if total_length % 2 == 1:
                    return max(l1,l2)
                    
                else:
                    return (max(l1 ,l2)+ min(r1,r2))/2
                    
            elif l2 > r1:
                low = mid + 1
            else:
                high = mid -1
        return -1


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna