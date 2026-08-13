# Last updated: 8/13/2026, 8:27:02 PM
class Solution(object):
    def setZeroes(self, matrix):

        first_row_zero=False
        first_col_zero=False

        for i in matrix[0]:
            if i == 0:
                first_row_zero= True
                break
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
    
        for k in range(1,len(matrix)):
            for l in range(1,len(matrix[k])):
                if matrix[k][0]== 0 or matrix[0][l] == 0:
                    matrix[k][l] = 0
        if first_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if first_row_zero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        return matrix
            