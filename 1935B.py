from collections import Counter
t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    d = Counter(l)
    