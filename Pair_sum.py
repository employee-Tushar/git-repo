
list1=[2,4,6,8,9,3,2,4,5,3,7]
n=len(list1)
k=10

for i in range(n):
    for j in range(i+1,n):
        if(list1[i]+list1[j]==k):
            print(list1[i],list1[j])
