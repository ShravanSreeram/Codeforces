#99A in right, 139 A in link

n = int(input())
l = list(map(int, input().split()))
k = sum(l)
#n = n - ((n//k)*k)
n=n%k +k
i = 0
while 1:
    n = n-l[i]
    if n <= 0:
        print(i+1)
        break
    i = (i+1)%len(l)
    
