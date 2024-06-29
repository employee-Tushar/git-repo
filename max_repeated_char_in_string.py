
s="dfksdflksfkddsf"

ch={}

for i in s:
    if i in ch:
        ch[i]+=1
    else:
        ch[i]=1


print(ch)

min_char=min(ch, key=ch.get)

max_char=max(ch, key=ch.get)

print("Min Char:",min_char)
print("Max char:",max_char)