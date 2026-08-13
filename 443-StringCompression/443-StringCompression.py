# Last updated: 8/13/2026, 8:23:33 PM
class Solution(object):
    def compress(self, chars):
        i = 0
        j = 0 
        n= len(chars)
        while j < n :
            charr = chars[j]
            count = 0
            while j < n and chars[j] == charr:
                count += 1
                j += 1
            chars[i] = charr
            i += 1
            if count > 1:
                 for k in str(count):
                     chars[i] = k
                     i += 1
                     
        return i
              
        