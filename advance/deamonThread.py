from threading import Thread, current_thread
def disp():
    print("Deamon Thread")
mt=current_thread()
print(mt.getName())
print("MT :",mt.isDaemon())
t1=Thread(target=disp)  
print("Before",t1.isDaemon())  #check thread damon or not
print("Before",t1.daemon) 
t1.setDaemon(True)
print("After",t1.isDaemon())
t1.start()  