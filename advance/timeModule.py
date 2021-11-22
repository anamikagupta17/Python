from time import time,ctime,localtime
epoch=time() #time    in seconds
print(epoch)  #seconds

et=ctime(epoch) #convert epoch and then return time date
print(et)
print(ctime()) #return current time
print()
tm=localtime()
print(tm)
print(tm.tm_year)
print(tm.tm_hour)
print(tm.tm_min)

