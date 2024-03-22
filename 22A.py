k = int(input())
l = list(map(int,input().split()))
l.sort()
if len(set(l))==1:
    print("NO")
else:
    for i in range(1,len(l)):
        if l[i] != l[0]:
            print(l[i])
            break
