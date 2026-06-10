# ---------USING SLIDING WINDOW---------------------
def maxsubArray(n,k):
    i = 0
    max_length = 0
    sum = 0
    for j in range(len(n)):
        sum += n[j]
        while(sum > k):
            sum -= n[i]
            i += 1
        if sum == k:
            length = j - i+1
            max_length = max (length,max_length) 
    return max_length
print(maxsubArray([1,6,5,8,11],19))

# ---------USING PREFIX SUM(HASH MAP)---------------------

def maxxSubarray(n,k):
    sum = 0
    max_length = 0
    map = {}
    for i in range(len(n)):
        sum += n[i]
        if sum == k:
            max_length = max(max_length,i+1)

        if (sum-k) in map:
            length = i - map[sum-k]
            max_length = max(length,max_length)
        if sum not in map:
            map[sum] = i
    return max_length 

print(maxxSubarray([-2,6,5,8,11],19))
