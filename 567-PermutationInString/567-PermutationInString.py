# Last updated: 8/13/2026, 8:22:52 PM
class Solution(object):
    def checkInclusion(self, s1, s2):
        from collections import Counter
        need = Counter(s1)
        n = len(s1)
        left = 0
        cur_freq = {}
        for i in range(len(s2)):
            cur_freq[s2[i]] = cur_freq.get(s2[i],0)+1
            while (i-left+1) > n:
                cur_freq[s2[left]] -= 1
                if cur_freq[s2[left]] == 0:
                    del cur_freq[s2[left]]
                left += 1

            if i-left+1 == n:
                if cur_freq == need:
                    return True
        return False
            
            