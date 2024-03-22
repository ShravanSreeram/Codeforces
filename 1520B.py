l =[1,11,111,1111,11111,111111,1111111,11111111,111111111,1111111111]
prev = [0,9,18,27,36,45,54,63,72,81]

n = int(input())
for i in range(n):
    k = (input())
    print(prev[len(k)-1]+(int(k)//l[len(k)-1]))
    # count =0 
    # for j in range(1,k):
    #     if len(set(str(j)))==1:
    #         count+=1
    # print(count)
    