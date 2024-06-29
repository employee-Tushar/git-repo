


a=int(input("Enter the number:"))
d={}
for i in range(a):
    s=input("Enter the word:")
    if s in d:
        d[s]=d[s]+1
    else:
        d[s]=1
print(len(d))
# print(*d.values())
print(d)


# a=int(input("Enter the number:"))
# d={}
# for i in range(a):
#     s=input("Enter the word:")
#     if s in d:
#         d[s]+=1
#     else:
#         d[s]=1
# print(len(d))
#
# l=d.values()
# b=(' '.join(map(str,l)))
# print(b)

