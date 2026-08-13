# Last updated: 8/13/2026, 8:23:30 PM
class Solution(object):
    def frequencySort(self, s):
        from collections import Counter

        freq = Counter(s)
        sortedValues = sorted(freq.items(), key = lambda x:-x[1])
        newlist = [count * values for values,count in sortedValues]
        return "".join(newlist)
       


    

        