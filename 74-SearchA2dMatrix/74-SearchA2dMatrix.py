# Last updated: 8/13/2026, 8:27:01 PM
class Solution(object):
    def searchMatrix(self, matrix, target):
        for row in matrix:
            l,r = 0,len(row)-1
            if row[l] <= target <= row[r]:
                while l <= r:
                    mid = (l+r)//2
                    if row[mid] == target:
                        return True
                    if row[mid] > target:
                        r = mid -1
                    else:
                        l = mid + 1
        return False