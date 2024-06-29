#
# l1="Ram is a good boy"
#
# a= l1.split()
#
# l2=a[::-1]
#
# print(l2)


a=input("Enter a string:")
l=""
for i in a:
    if (i>='A' and i<='Z') | (i>='a' and i<='z') | (i==' ') |(i>='0' and i<='9'):
        l=l+i
print(l)