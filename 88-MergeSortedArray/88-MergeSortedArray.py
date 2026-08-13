# Last updated: 8/13/2026, 8:26:39 PM
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        left = n-1
        tail = ( m + n )- 1
        mid = m-1
        while mid >= 0 and left >= 0:
            if nums2[left] > nums1[mid]:
                nums1[tail] = nums2[left]
                left -= 1
                tail -= 1
            else:
                nums1[tail] = nums1[mid]
                mid -= 1
                tail -= 1

        while left >= 0:
            nums1[tail] = nums2[left]
            left -= 1
            tail -= 1
        return nums1
        
                
                
            
                

        