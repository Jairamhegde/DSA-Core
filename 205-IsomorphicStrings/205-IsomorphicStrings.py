# Last updated: 8/13/2026, 8:25:06 PM
class Solution(object):
    def isIsomorphic(self, s, t):
        smap = {}
        tmap = {}
        for i in range(len(s)):
            if s[i] not in smap:
                smap[s[i]] = i
            if t[i] not in tmap:
                tmap[t[i]] = i
            if smap[s[i]] != tmap[t[i]]:
                return False
        return True



        