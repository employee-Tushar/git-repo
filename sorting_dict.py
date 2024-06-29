

dict1={ 111:"lucky", 555:"Tushar", 666:"Shaitaan", 444:"Sahoo"}

d=sorted(dict1.keys())
dict2={}

print(d)

for i in d:
    dict2[i]=dict1[i]

print(dict2)