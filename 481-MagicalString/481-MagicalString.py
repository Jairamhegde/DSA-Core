# Last updated: 8/13/2026, 8:23:20 PM
class Solution(object):
    def magicalString(self, n):
        if n <= 0 :
            return 0 
        if n <= 3:
            return 1
        new = [1,2,2]
      
        count = 1
        i = 2
        j = 2
        while j < n  :
            element = new[-1]
            corres = 1 if element == 2 else 2
            for m in range(new[i]):  
                j += 1
                if j >= n:
                    break
                if corres == 1:
                    count += 1
                new.append(corres) 
            i += 1
        return count
   
            