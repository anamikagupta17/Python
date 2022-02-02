n=int(input("Enter a nuber "))

if n>1:
    for i in range(2,int(n/2)+1):
        if(n%i ==0):
            print(n,'is not prime number')
            break
    else:
        print(n,'is prime number')

else:
     print(n,'is not prime number')   