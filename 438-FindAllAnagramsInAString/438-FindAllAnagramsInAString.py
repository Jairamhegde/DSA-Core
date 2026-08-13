# Last updated: 8/13/2026, 8:23:35 PM
class Solution(object):
    from collections import Counter
    def findAnagrams(self, s, p):
        new = []
        needed = Counter(p)
        current = {}
        left = 0
        for i in range(len(s)):
            current[s[i]] = current.get(s[i],0)+1
            while (i - left + 1) > len(p):
                current[s[left]] -= 1
                if current[s[left]] == 0:
                    del current[s[left]]
                left += 1
         
            if current == needed:
                new.append(left)
        return new 

        