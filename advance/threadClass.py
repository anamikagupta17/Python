from threading import*
from time import sleep
class Student(Thread):  #thread is parent class
    def __init__(self,a):
        Thread.__init__(self) # calling parent (thread) class constructor
        self.a=a
        print("Child Thread Constructor")
        print("Self Parameter",self.a)
    def run(self):  # it call automatic when thread start
        print("Run Method")
        for i in range(5):
            print("Child Thread")

t=Student(10)
print(t.name)
t.start()
t.join() # first completly execute t thread after that main thread will execute
print("Main Thread :",current_thread().name)


print()
print("Create Thread without child class")


class Anamika():
    def disp(self):
        print("Thread")



a=Anamika()
th=Thread(target=a.disp)
th.start()

print()
print("Single Tasking Using Thread")
class MyEaxm():
    def solved_ques(self):
        self.q1()
        self.q2()
        self.q3()

    def q1(self):
        print("Question 1 solved")    
        sleep(1)
    def q2(self):
        print("Question 2 solved")    
        sleep(1)
    def q3(self):
        print("Question 3 solved")  
        sleep(1)          

my=MyEaxm()
thr=Thread(target=my.solved_ques)
thr.start()


print()
print("Multi Tasking Using Multi Thread")
print("Two Task 2 Thread")
class Hotel:
    def __init__(self,t):
        self.t=t
        self.l=Lock()
    def food(self):
        self.l.acquire()
        for i in range(1,6):
            print(self.t,i)    
        self.l.release()

h1=Hotel("Take Order from table ")      
h2=Hotel("Server Order to table ")  
t1=Thread(target=h1.food)      
t2=Thread(target=h2.food)  
t1.start()
t2.start()