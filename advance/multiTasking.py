#thread
import threading
from threading import Thread,current_thread
t=threading.current_thread().getName()  # return current thread 
print(t) #main thread
print("Anamika Gupta")

print("Create Thread")

def disp(a,b):
    print("Thread Running ",a,b)

t=Thread(target=disp,args=(10,20)) # create thread , args should be tuple
t.start() #start the thread

for i in range(3):
    t=Thread(target=disp,args=(10,23)) #args should be tuple

    t.start() #start the thread

print("Set and Get Thread Name")
def disp2():
    print("Defult Child Thread Name :", current_thread().getName())  # will return 5 becuse 4 used above
    current_thread().setName("Ana Child Thread")  #set thread name
    print("New Child Thread Name ",current_thread().getName())
    print("Child Thread Name by name property ",current_thread().name)
    current_thread().name="Flying Thread"
    print("New Child Thread Name by name property ",current_thread().name)


tt=Thread(target=disp2)
print("Default Child :",tt.getName()) # we can get like this also cans et also by setName
tt.start()    
print("Main Thread  Name:",current_thread().getName())
current_thread().setName("Ana Main Thread")
print("New Main Thread Name ",current_thread().getName())

