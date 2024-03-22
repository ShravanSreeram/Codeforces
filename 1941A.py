t = int(input())
for i in range(t):
    l,r,k = map(int,input().split())
    l1 = list(map(int,input().split()))
    r1 = list(map(int,input().split()))
    '''
    d = {}
    for i in l:
        d[i]=0
    '''
    s =0
    for i in range(len(l1)):
        for j in range(len(r1)):
            if l1[i]+r1[j] <= k:
                s+=1
    print(s)