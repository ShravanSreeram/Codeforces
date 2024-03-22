m,s = map(int,input().split())
k=int(s)

if m==1 and s==0:
    print(0,0)
elif s<1 or s> 9*m:
    print("-1 -1")
#min
else:
    min = [0 for i in range(m)]
    min[0] = 1
    s=s-1
    for i in range(m-1,-1,-1):
        if s>9:
            min[i]=9
            s = s-9
        else:
            min[i] = min[i]+s
            break
    for i in range(0,m):   
        print(min[i],end='')    
    print(end=' ')
    max1=[0 for i in range(m)]
    for i in range(0,m):
        if k>9:
            max1[i]=9
            k = k-9
        else:
            max1[i] = max1[i]+k
            break
    for i in range(0,m):
        print(max1[i],end='')