num=[2,7,11,15]
target=26
def twoSum(num,target):
    for i in range(len (num)):
        for k in range(len(num)):
            if (num[i]+num[k])==target:
                return [i,k]
            
print(twoSum(num,target))