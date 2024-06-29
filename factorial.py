

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact


def sum_of_factorial_of_the_digits(start,end):
    for i in range(start,end):
        sum=0
        b=i
        while(i>0):
            r=i%10
            sum+=factorial(r)
            i=i//10
        if(sum==b):
            print(sum)

a=int(input("Enter a start range:"))
b=int(input("Enter a end range:"))
sum_of_factorial_of_the_digits(a,b)