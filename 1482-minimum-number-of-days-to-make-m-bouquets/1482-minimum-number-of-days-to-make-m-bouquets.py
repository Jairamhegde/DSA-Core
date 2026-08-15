class Solution(object):
    def minDays(self, bloomDay, m, k):
        def check(bloomDay,m,k,d):
            left = 0
            bkt = 0
            for i in range(len(bloomDay)):
                if i-left+1 >= k and bloomDay[i]<=d:
                    bkt+= 1
                    left = i+1
                if bkt == m:
                    return True
                if bloomDay[i] > d:
                    left = i+1
            return False
        
        answer = -1
        low ,high = 1,max(bloomDay)
        while low <= high:
            mid = (low+high)//2
            res = check(bloomDay,m,k,mid)
            print(res)
            if res:
                answer = mid
                high = mid-1
            else:
                low = mid + 1
        return answer
        