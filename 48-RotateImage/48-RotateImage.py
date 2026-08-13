# Last updated: 8/13/2026, 8:27:34 PM
class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for k in range(n):
            matrix[k].reverse()
        return matrix
        