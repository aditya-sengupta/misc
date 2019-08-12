def collatz(x):
    if(x%2==0):
        return x/2
    return (3*x)+1

def itercount(x, L):
    c = collatz(x)
    if (x==1):
        return 1
    if(L[c]!=0):
        L[x] = L[c] + 1
    else:
        L[x] = itercount(c, L)
    return L[x]

countlist = [0] * 1000000
countlist[1] = 1
for i in range(1, 10):
    cstep = 0
    if(countlist[i]==0):#not filled in by previous iteration
        cstep += 1
        countlist[collatz(i)]

print(countlist.index(max(countlist)))
