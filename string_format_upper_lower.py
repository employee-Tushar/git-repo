
def stringFormat(s):
    l=[]
    temp= s.split('_')
    #print(temp)
    for i in temp:
        l.append(i[0].lower()+i[1:].upper())
    s='.'.join(l)
    print(s)


n="This_Is_A_Good_Morning"
stringFormat(n)


def stringFormat(s):
    a=""
    temp= s.split('_')
    #print(temp)
    for i in temp:
        s=s+(i[0].lower()+i[1:].upper())
    s='.'.join(l)
    print(s)


n="This_Is_A_Good_Morning"
stringFormat(n)