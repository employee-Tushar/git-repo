def Fizz_program(n):

    for i in range(n):
        if (i%3==0 and i%5!=0):
            print("Fizz")

        elif (i%5==0 and i%3!=0):
            print("Buzz")

        elif (i%15==0):
            print("FizzBuzz")

        else:
            print(i)

a=int(input("Enter a number:"))
Fizz_program(a)
