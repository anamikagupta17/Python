import time
from dateTime import date
for i in range(20):
    print(i)
    if i==10:
        time.sleep(2)


dob=date(1996,5,17)  
today=date.today()
age=today.year-dob.year-((today.month,today.day)< (dob.month,dob.day)) 
print("age")     
print(age)
print(2-False) #False=0,True=1
print(2-True)