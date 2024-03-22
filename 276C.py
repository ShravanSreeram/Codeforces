#1500 rating
def sort_with_priority(original_list, priority_dict):
    # Sort the original list based on the priority provided in the dictionary
    return sorted(original_list, key=lambda x: -priority_dict.get(x, float('-inf')))

# Example usage:
original_list = [3, 1, 2, 4]
priority_dict = {1: 3, 2: 1, 3: 2, 4: 4}

sorted_list = sort_with_priority(original_list, priority_dict)
print(sorted_list)  # Output: [4, 1, 3, 2]



n,q = map(int,input().split())
li = list(map(int,input().split()))
d=dict([[i,0]for i in range(n)])

for i in range(q):
    l,r = map(int,input().split())
    l,r = l-1,r-1
    for j in range(l,r+1):
        d[j]+=1


print(d,li)
li = sort_with_priority(li,d)
print(li)