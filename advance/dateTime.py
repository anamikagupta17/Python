from datetime import datetime,date,time, timedelta
dt=datetime(year=2020,month=8,day=30,hour=15,minute=23)
dt2=datetime(2021,4,6,2,45)
print(dt)
print(dt2)
print(dt2.day)
print(datetime.now()) #current date and time timezone
ct=datetime.now()
print(ct.day)
ctt=datetime.today()
print(ctt)

print("Date")
dte=date(2021,12,2)
print(dte)
print(date.today())
print(dte.year)


print("Time")
tm=time(hour=15,minute=30,second=30)
print(tm)
print(tm.hour)

print("Time delta")
td=timedelta(days=10)  #by default every thing 0
d=datetime.today()
print(d+td)  #incremnet date wise
print(d-td)   #subtract date wise

print("Compare date")
d1=date(year=2020,month=10,day=15)
d2=date(year=2021,month=9,day=25)
print(d1==d2)
print(d1 > d2)
print(d1 < d2)
print(d1 != d2)
