# Last updated: 8/13/2026, 8:25:40 PM
class Solution(object):
    def compareVersion(self, version1, version2):
        v1ar = version1.split(".")
        v2ar = version2.split(".")
        
        v1 = int(v1ar[0])
        v2 = int(v2ar[0])
        if v1 > v2 :
            return 1
        if v1 < v2:
            return -1
        i = j = 0
        while i < len(v1ar) and j < len(v2ar):
            val1 = int(v1ar[i])
            val2 = int(v2ar[j])
            if val1 > val2 :
                return 1
            if val1 < val2:
                return -1
            i += 1
            j += 1
        while i < len(v1ar):
            if int(v1ar[i]) > 0:
                return 1
            i += 1

        while j < len(v2ar):
            if int(v2ar[j]) > 0:
                return -1
            j += 1
        return 0
            