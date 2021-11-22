a=10
b=20

if(b): print(b)	
if(a<b):
    print('Less')	
    print('10 is less then 20')	
print("Rest Of the code");
	
a=int(input("Enter number greater than 2 : "))
if(a>2):
	print(" you have enetered",a)
	
	
#nested if 	

if(a):
	print(a)
	if(a >2):
		print("Greater then 2")
	if(a < 2):
		print("less then 2")
	if(a == 4):
		print("Equal to")	
print('Nested if')
a1=3
b1=4
c1=6	
if(a1<b1 and b1<c1):	
	print('Both condition True "AND"')
	
if(a1<b1 or b1>c1):	
	print('Any one condition True "OR"')	
	
#if else
a=int(input("Enter number greater than 2 : "))
if(a >2):
	print("Correct Input")
else:
	print('Worng Input')
print()	
print("Correct Input Value") if	(a >2) else print('Worng Input Value')  #single line statement
#elif
if(a<2):
	print("Enter number is greater than 2")
elif(a <5 and a>2):
	print("Enter number is greater than 5")
elif(a >7 and a<21):	
	print("Enter number is greater than 7")
elif(a >21):	
	print("Enter number is greater than 21")
else:
    print("else")	
n=2	
while(n <=20):
		print(n)
		n+=2
else:
	print('while executed')		
		
		