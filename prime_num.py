


def prime(start, end):
    z = 0
    for n in range (start, end):
        for i in range(2,n//2+1):
            if n%i==0:
                z=1
                break
        else:
            print(n)

# a=int(input("Enter a number:"))

prime(3,20)