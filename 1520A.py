t= int(input())
for i in range(t):
    n = int(input())
    s = input()
    set1 = set()
    set1.clear()
    if n==1 or len(set(list(s))) == len(s):
        print("YES")
    else:
        le = 0
        while le < n:
            if s[le] in set1 and le<n:
                print("NO")
                break
            else:
                if s[le] not in set1 and le<n:
                    set1.add(s[le])
                    count =0
                    while  (le+count) < n and s[le+count] == s[le] :
                        count+=1
                    le+=count  
            if le >=n:
                continue
            #print(set1,s[le],le)
        else:
            print("YES")
            