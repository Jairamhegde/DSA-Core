# Last updated: 8/13/2026, 8:26:34 PM
class Solution(object):
    def generate(self, numRows):
        triangle = []
        for i in range(numRows):
            new = [1]*(i+1)
            
            for j in range(1,i):
                new[j] = triangle[i-1][j] + triangle[i-1][j-1]
            triangle.append(new)
        return triangle
        