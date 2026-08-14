class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
        def check(piles,h,k):
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / k)
            if total_hours <= h:
                return True
            else:
                return False
        max_pile = max(piles)
        low,high = 1,max_pile
        answer = max_pile
        while low <= high :
            mid = (low + high )//2
            res = check(piles,h,mid)
            if res:
                answer = min(answer,mid)
                high = mid -1
            else:
                low = mid + 1
        return answer
