class Solution(object):
    def reversePairs(self, nums):
        def merge(ary,l,m,h):
            reverse_pair = 0
            new = []
            left=l
            right = m+1 
            mi = left
            for k in range(m+1,h+1):
                while mi <= m and ary[mi] <= 2*ary[k]:
                    mi += 1
                if mi <= m:
                    reverse_pair += (m - mi + 1)
            while left <= m and right <= h:
                if ary[left] > ary[right]:
                    new.append(ary[right])
                    right += 1
                else:
                    new.append(ary[left])
                    left += 1
            while left <= m:     
                new.append(ary[left])
                left += 1
            while right <= h:
                new.append(ary[right])
                right += 1
            for i in range(l,h+1):
                ary[i] = new[i-l]
            return reverse_pair
        def mergeSort(ary,low,high):
            count = 0
            if low >= high:
                return count
                
            mid = (low+high)//2
            count += mergeSort(ary,low,mid)
            count += mergeSort(ary,mid+1,high)
            count += merge(ary,low,mid,high)

            return count
            
        return mergeSort(nums,0,len(nums)-1)
        
                    

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna