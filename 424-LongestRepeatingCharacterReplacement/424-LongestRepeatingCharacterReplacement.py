# Last updated: 8/13/2026, 8:23:43 PM
class Solution(object):
    def characterReplacement(self, s, k):
        hash = {}
        max_length = float('-inf')
        max_freq = 0
        left = 0

        for i in range(len(s)):
            hash[s[i]] = hash.get(s[i],0)+1
            max_freq = max(max_freq,hash[s[i]])
            
            while left < len(s) and (i - left + 1)-max_freq > k:
                hash[s[left]] -= 1
                left += 1

            max_length = max(max_length,(i-left + 1))

        return max_length
            
        