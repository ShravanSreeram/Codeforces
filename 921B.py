def find_largest_factor(N, K):
    ans = 0
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            if i <= K:
                ans = max(ans, i)
            if N // i <= K:
                ans = max(ans, N // i)
    return ans
t = int(input())
for i in range(t):
    x,n = map(int,input().split())
    div = x//n
    if div <0:
        print(0)
    elif div==1:
        print(1)
    else:
        #while x%div !=0:
        #    div-=1
        div = find_largest_factor(x,div)
        print(div)