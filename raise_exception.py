#Raise exception if element is 1 in list

list1=[2,4,3,6,7,5]
sum=0
for i in list1:
    if i==1:
        raise Exception("Exception: 1 is found")
    else:
        sum+=i

print("Sum:",sum)