# 🟡 #2195 - 2195. Append K Integers With Minimal Sum

## Problem Info
| Field | Value |
|-------|-------|
| **Difficulty** | Medium |
| **Topics** | Array, Math, Greedy, Sorting |
| **Language** | Unknown |
| **Runtime** | N/A |
| **Memory** | N/A |
| **Solved** | 8/19/2026 |

## Solution
```txt
                    required = k - aded
                    total += required * ((prev+1)+ (prev + required))//2

                    return total
            prev = current
        gap = k-aded
            total += gap * ((nums[-1]+1) + (nums[-1]+gap))//2
        return total
        
                elif count_int > k:
        if gap > 0:
        

```



---
*Auto-synced by [LeetPush](https://github.com/yourusername/leetpush) 🚀*
