def gib(num,n1,n2):
    if num < 0:
        print("Wrong Value")
    else:
        if num <= 1:
            print(num) 
        else:
            for i in range(1, num):
                n3 = n2 - n1
                n1 = n2
                n2 = n3
            print(n3)  
    
gib(10,0,1)