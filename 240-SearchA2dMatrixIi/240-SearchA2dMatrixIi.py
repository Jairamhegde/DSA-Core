# Last updated: 8/13/2026, 8:24:31 PM
class Solution(object):
    def searchMatrix(self, matrix, target):
        row,colum = 0,len(matrix[0])-1
        while row <len(matrix) and colum >= 0:
            element = matrix[row][colum]
            if element == target:
                return True
            elif element > target:
                colum -= 1
            else:
                row += 1
        return False
        