# Last updated: 8/13/2026, 8:24:02 PM
class Solution(object):
    def topKFrequent(self, nums, k):
        
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+1
        print(freq)

        bucket = [[] for _ in range (len(nums)+1)]
        for key,value in freq.items():
            bucket[value].append(key)
        new = []
        for j in range(len(bucket)-1,-1,-1):
            for l in bucket[j]:
                new.append(l)
                if len(new) == k:
                    return new



        
        