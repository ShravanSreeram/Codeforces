# 1221A . Asked in Round 73 (div 2)
t = int(input())
for i in range(t):
    d={1:0,2:0,4:0,8:0,16:0,32:0,64:0,128:0,256:0,512:0,1024:0,2048:0}
    n = int(input())
    l = list(map(int, input().split()))
    for j in l:
        if j<=2048:
            d[j]+=1
    if d[2048] >0:
        print("YES")
    else:
        for j in d:
            if d[j] >= 2:
                d[2*j] += (d[j]//2)
            if d[2048] >0:
                print("YES")
                break
        else:
            print("NO")