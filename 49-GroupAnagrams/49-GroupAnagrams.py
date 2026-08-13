# Last updated: 8/13/2026, 8:27:30 PM
class Solution(object):
    def groupAnagrams(self, strs):
        d={}
        for word in strs:
            hash=[0]*26
            for char in word:
                index=ord(char)-97
                hash[index]+=1
            key=tuple(hash)
            if key not in d:
                d[key]=[]
            d[key].append(word)
        return d.values()
        