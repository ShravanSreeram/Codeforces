t = int(input())
for i in range(t):
    n,r,b = map(int,input().split())
    uniform_div = r//(b+1)
    l = [uniform_div for i in range(b+1)]
    remainder = r%(b+1)
    for i in range(len(l)):
        if remainder==0:
            break
        else:
            l[i]+=1
            remainder-=1
    #print(l)
    for i in range(len(l)):
        if i!= len(l)-1:
            print(l[i]*'R',end='B')
        else:
            print(l[i]*'R')
