# Last updated: 8/13/2026, 8:27:05 PM
class Solution(object):
    def plusOne(self, digits):
        element = 0
        for i in digits:
            element = element * 10 + i
        
        return [int(i) for i in str(element+1)]
            