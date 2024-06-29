
list1=[4,1,67,34,233,3,5,4]

# list1.sort()
#
# print(list1)

n=len(list1)
for i in range(n):
    for j in range(i,n):
        if(list1[i]>list1[j]):
            list1[i],list1[j]=list1[j],list1[i]

print(list1)