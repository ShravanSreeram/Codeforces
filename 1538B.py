t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    if sum(l)%len(l)!=0:
        print(-1)
    else:
        count = 0
        avg = sum(l)//len(l)
        for j in range(n):
            if l[j]>avg:
                count += 1
        print(count)