k = int(input())
for i in range(k):
    n,s,r = map(int, input().split())
    n=n-1
    g=s-r
    s=r
    l = [s//n for x in range(n)]
    l[0] += (s-(s//n)*n)
    l.append(g)
    print(*l)