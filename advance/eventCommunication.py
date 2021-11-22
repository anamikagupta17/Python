#event thread
from threading import*
from time import sleep
def light_switch():
    sleep(3)
    e.set()
    print("Green Light On")
    sleep(5)
    print("Red Light On")
    e.clear()

def traffic():
    e.wait()
    while e.is_set():
        print("You can go...")    
        sleep(.5)
    print("Program done")    

e=Event()    
t1=Thread(target=light_switch)
t2=Thread(target=traffic)
t1.start()
t2.start()
