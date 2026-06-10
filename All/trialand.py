
Input= ["eat","tea","tan","ate","nat","bat"]
def groupAnagram(n):
    d={}
    for word in n:
        hashlist=[0]*26 
        for charector in word:
            index=ord(charector)-97
            hashlist[index]+=1
        key=tuple(hashlist)
        if key not in d:
            d[key]=[]
        d[key].append(word)
    return d.values()

print(groupAnagram(Input))

