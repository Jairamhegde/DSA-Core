a="listen"  
b="silent"

def check(a,b):
    d1={}
    d2={}
    for i in a:
        d1[i]=d1.get(i,0)+1
    for j in b:
        d2[j]=d2.get(j,0)+1
    # print(d1,d2)
    for i in a:
        if d1[i]==d2[i]:
            return True
        return False

print(check(a,b))