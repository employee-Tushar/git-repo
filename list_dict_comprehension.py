
l=[]
for i in range(10):
    if(i%2):
        l.append(i)
print(l)



ls = [i for i in range(10) if i % 2 == 0]
print(ls)




dic2={}
for i in range(10):
    if(i%2):
        dic2[i]=i*i

print(dic2)



dic1={n:n*n for n in range(10)}

print(dic1)