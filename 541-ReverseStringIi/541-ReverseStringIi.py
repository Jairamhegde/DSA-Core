# Last updated: 8/13/2026, 8:22:59 PM
class Solution(object):
    def reverseStr(self, s, k):

        new = list(s)

        for i in range(0,len(s),2 * k):
            start = i
            end = min(i + k-1,len(s)-1)
            while (start < end):
                new[start],new[end] = new[end],new[start]
                start += 1
                end -= 1
        return "".join(new)

        
        