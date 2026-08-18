# 🟢 #2195 - 1539. Kth Missing Positive Number

## Problem Info
| Field | Value |
|-------|-------|
| **Difficulty** | Easy |
| **Topics** | Array, Binary Search |
| **Language** | Unknown |
| **Runtime** | N/A |
| **Memory** | N/A |
| **Solved** | 8/19/2026 |

## Solution
```txt
class Solution(object):
    def findKthPositive(self, arr, k):
        low = 0
        high = len(arr)-1
        while low <= high:
            mid = (low + high )//2
            missing = arr[mid] - mid -1
            if missing >= k:
                high = mid - 1
            else:
                low = mid + 1
        return low + k
        


```



---
*Auto-synced by [LeetPush](https://github.com/yourusername/leetpush) 🚀*
