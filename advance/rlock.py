from threading import*
class Flight:
    def __init__(self,avail_seat):
        self.avail_seat=avail_seat
        #self.l=Lock()
        #self.l=RLock()
        self.l=Semaphore(2)
    def reserve(self,need_seat):
        self.l.acquire()
        print(self.l.value)
       # self.l.acquire()  # 2nd in RLock
        print("Availabe Seat : ",self.avail_seat)
        if(self.avail_seat >= need_seat):
            name=current_thread().name
            print(f'{need_seat} seat is alloted for {name}')
            self.avail_seat-=need_seat

        else:
            print("Sorry No seat available")   

        self.l.release()
       # self.l.release()   # 2nd in RLock or Semaphore
f=Flight(3)     
t1=Thread(target=f.reserve,args=(1,),name="Anamika")     
t2= Thread(target=f.reserve,args=(1,),name="Pramod")       
t3= Thread(target=f.reserve,args=(1,),name="Rock")          
t1.start()
t2.start()
t3.start()