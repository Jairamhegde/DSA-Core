st="maadaam"
def checkPalendrome(st,i=0,j=None):
    if (j==None):
        j=len(st)-1
    if(i<j):
        if(st[i]==st[j]):
            i+=1
            j-=1
            return checkPalendrome(st,i,j)
        return False
    return True
print(checkPalendrome(st=st))

 
        
