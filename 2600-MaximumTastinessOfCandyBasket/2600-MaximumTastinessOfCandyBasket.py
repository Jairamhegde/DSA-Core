# Last updated: 8/14/2026, 1:07:47 AM
class Solution(object):
    def maximumTastiness(self, price, k):
        price.sort()
       
        def check(price,k,distance):
            t = 1
            left = 0
            for i in range(1,len(price)):
                if (price[i] - price[left]) >= distance:
                    t += 1
                    left = i
                    
                    if t == k:
                        return True
                    
            return False
        
        low,high = 0,(price[-1] - price[0])
        answer = 0
        while low <= high:
            mid = (low+high)//2
            res = check(price,k,mid)
            if res:
                answer = mid
                low = mid + 1
            else:
                high = mid -1
        return answer
        
        
        