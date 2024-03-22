n = int(input())
for i in range(n):
    k = int(input())
    l = list(map(int,input().split()))
    flag=1
    avg = sum(l)//k
    for i in range((k+1)//2):
        if l[i] < avg:
            flag=0
    if k==1:
        print("YES")
    elif flag and sum(l):
        print("YES")
    else:
        print("NO")