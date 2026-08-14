# Last updated: 8/15/2026, 1:18:18 AM
'''
Pattern : Binary Search on answer
time complexity : Time complexity: O(n × log(max(piles)))
'''

1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3    
4        def check(piles,h,k):
5            total_hours = 0
6            for pile in piles:
7                total_hours += math.ceil(pile / k)
8            if total_hours <= h:
9                return True
10            else:
11                return False
12        max_pile = max(piles)
13        low,high = 1,max_pile
14        answer = max_pile
15        while low <= high :
16            mid = (low + high )//2
17            res = check(piles,h,mid)
18            if res:
19                answer = min(answer,mid)
20                high = mid -1
21            else:
22                low = mid + 1
23        return answer
24