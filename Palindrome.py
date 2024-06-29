
s=input("Enter a string or Number to check if its Palindrome or not:")

# if (s==s[::-1]):
#     print("Palindrome")
# else:
#     print ("Not Palindrome")


n=len(s)
z=0

for i in range(n):
    if(s[i]!=s[n-i-1]):
        z=1
        break

if(z==0):
    print("Palindrome")
else:
    print("Not Palindrome")