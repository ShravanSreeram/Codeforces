t=int(input())
s=''
for i in str(t):
    if  s or i!='9':
        k = 9-int(i)
        s+= min(str(k),(i))
    else:
        s+=i
print(s)    