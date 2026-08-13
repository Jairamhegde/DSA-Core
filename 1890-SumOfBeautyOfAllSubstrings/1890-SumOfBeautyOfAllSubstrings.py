# Last updated: 8/13/2026, 8:21:18 PM
class Solution(object):
    def beautySum(self, s):
        total = 0
        for i in range(len(s)):
            freq = {}
            for j in range(i,len(s)):
                freq[s[j]] = freq.get(s[j],0)+1

                minval = min(freq.values())
                maxval = max(freq.values())
                total += (maxval - minval)
        return total

        