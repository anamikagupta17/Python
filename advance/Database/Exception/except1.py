a=10
b=0
try:
    c=a/b
    print(c)
except ZeroDivisionError:  # we can also alias  ZeroDivisionError as ae and can print ae also
    print("can't divide by 0")  
except NameError:
    print("g not defiend")    
else :
    print("else part")
finally:
    print("FInally Block")        
print("rest of the code")