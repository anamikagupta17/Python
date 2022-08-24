#advance
*** when we write any function inside the class then we call it method 
*** when we write any function outside class then we call it function

opps(object oriended method)(we can say it is a structure or model)
1.Encapusulation :
2.Abstraction : user can see only needed thing (others are hidden): this whole functioanlity(show and hide) is Abstraction
3.Inheritance:
4.Polymorphism: one things used for many functioanlity 
eg : different input will give different output using a single function

we can say these all are 4 pillers of oops

class : group of attributes(variables) and mehtods(function)
eg: class Classname(object): object is optional(by default it will be there) ,object is base class(super class/parent class)
object: eg: obj_name=class_name()
def __init__(self):
    self.variable_name=2;
this is special function (constructor)    
self: is a variable which refer current object/instance ,first argument  always(means store adress of current object)
class object : each time create  copy of memory for every variable of class

constructor :  it call autoMATIC WHEN WE CREATE object. it called only one time  for a object

class variable :for accessing class variable we need class method, all object will have copy of same variable(if change in one place then  will chnage everywhere )
if we change it with object then it will change for that object only if we change it with the class then every where it will change
classmethod : for the class method 'cls' should be the first parameter
eg : @classmethod
     def methodname(cls):
         statements

methods
 1. Instance method : first parmamter shoud be self
     *Accessor: used for access and read data also called getter method
       eg: def get_value(self):
     *Mutator : this method used for modify,read,acess also called setter method
       eg : def set_value(self)
 2. Class method : for createing need to use decorator @classmethod, by default first parameter 'cls'(we can give any name)(but shoud be there first parameter)
    cls : refers the main class
    eg : @classmethod
     def methodname(cls):
         statements
 3. Static method : when we don't need object and class for performing any task (no default parameter)(need to use something from outside class)
  eg : @staticmethod   #without parameter
        def method_name()
        statements
  eg:   @staticmethod  #with parameter
        def method_name(f1,f2)
        print(f1,f2)

Inheritance
1 Single Inheritance  : derieved from only one base class    
2 Multi Level Inheritance : father->son->grandson
3 hierarchical Inheritance :father->son,daughter
4 Multiple Inheritance :   :Father,Mother ->child1 
eg: class childclassname(parentclassname) :
eg: class childclassname(parentclassname1,parentclassname2) :Multiple inheritance

*child class override methods and costructors of parent class if we create with same name
* if wanted to call methods and constructor of parent class in child class without overriding we can use 'super'

super(): used to call parent class constructor and methods and variables
MRO(method resolution oreder)(used in Multiple Inheritance)
  * first search in own class (child class)
  * when class inhrited from sevral classes then it search left to right
  * it wil not visit a class more than one(means only one time search in one class)


Polymorphism: many+forms  
 1. Duck Typing : functioanlity depend on object which object is passed
 2. Method override : same name  method in both child and parent class 
 3. Method Overloading : more then one method with same name  is defiend in same class in normal langauage(java) but 
 in python  if a method can perform more thaan one task then called method Overloading
 4. operator Overloading : if any opertaor perform additional action other that what it meant for
 (mans jis kaam ke liye define hua h uske alava bhi or bhi kaam kr raha h)

 hasattr(object,method): checks method or variable exists or not if found thn True else False
everything is define for every functioanlity like how + work for add
 + =int.__add__(self,other)=int,__add__(10,20)   : defined in int class
 + =str.__add__(self,other)=int,__add__('dfdf','fdsg')  : defined in str class
 we call them magic function

 modules: it is a file which contains group of variable,method,statements,class..
 syntax:  
1.import module_name or 
2.import module_name as alias or
3.from module_name import f1,f2,variable1,variable2....
4.from module_name import fun_name as f1...  eg f1()
5.from  module_name import*
eg: module_name.method(),method()->when import only function

** if same variable in many module then it will give prirotiy to the last import one 
eg :
from m1 import a
from m2 import a  
when we print a then it will print value of a defiend in second module m2


package: set of files (folder/directory) or also contain a package
 *package should(not neccessary version greater than2) have __init__.py file(esse pta chlta h ki wo package)(this file can we empty)
syntax:
 import packageName.module_name
 import packageName.subPakagename.module_name
 from packageName import module_name
 from packageName.subPakagename import module_name  eg : module_name.fun_name()
 from packageName.module_name import fun_name,variable,class...eg : fun_name()
 from packageName.subPakagename.module_name import fun_name,variable,class...  eg : fun_name()
 from packageName  import* used only for the packages define in __init__.py file
 from packageName.subPakagename import*  used only for the packages define in __init__.py file


 Abstact Class: Abstact class (ABC) derived from Abstact module(abc)
 Abstact Method: actions defined in child  class as per requirement
 Concrete Method: method define in abstract class
** we can not create object of abstract class
** if there is any abstract method in a class, that class must be abstract
** we can create norml method(called Concrete method)  in abstract class
** we  must need to define abstract method in child class  otherwise we need to make child class as abstract class
when we need to use same features of object then use abstract


Interface : in abstract class when we write only abstract method then it called Interface
when we need to use different features for different object
Interface slow as compare to abstract class

timedelta(): when we want to add date or subtract date
strftime(): format date and time
sleep(): stop execution of  program for few seconds 

MultiTasking:
1.Process Based  : multiple task at the same time where each task  separate independent program(process) eg: operating system level (like in system we open many aaps-notepad,wtsapp,chrome..)
2.Thread Based : multiple task at the same time where each task independent part of the same program eg: programming level (wordpad- writing,setting,spellcheck)

Thread: It is a separate flow of execution (we can say separate task), each task independent to each other
MultiThreading: Using multiple threads at the same time 
eg :  A bank app multiple ppl can access at the same time 

Main Tread : it is created when your program  starts(create by PVM  autoMATIC)
* we create thread without class it use own thread class and for starting  thread we need to start by start() method
* main thread first create child thread after that both thread start working separatly
* thread calls asynchronously(no sequence any one exceute any time)
Race Condition: sequence action unexpected so result is unreliable (wrong out)

Synchronization:
1.Lock : one thread lock only one time 
2.RLock: one thread acquire a lock many times (need to release as many time as you lock) 
(jisne lock kiya h vhi unclock kr skta h)
3.Semaphore: multiple thread can work together  and lock and release 

acquire(blocking=True, timeout=-1): lock the state
release() : release the state


Thread Communication: when 2 thread comunicate eachother
1.Event : one thread signal and other one wait for it
 set() ->set flag True
 clear()->reset/False flag anf block the flag
 wait(timeout=None) ->if flag true then  it start executing
2.Condition : used to improve speed of Communication between threads : associate with some kind of lock(locking workig automtic)
  notify(n=1)-> used to  immediatly wakeup one  thread  waiting on the condition
  notify_all()->same but for all thread
  wait(timeout=None)
3.Queue : same as Queue functionality(FIFO) it also ue lock method
  put()->used to Produce (means put data)
  get()->used for consume (means get data)
  empty()->check Queue empty or not


Deamon Thread : Continuously runs in backgound ,it support non -deamon thread
eg : in exam whole faily,teachers supports student for the exam : student->non-deamon thread and family,teacher ->deamon thread
setDeamon(True) or Deamon=True : create deamon thread for non-deamon Change true to false or vice versa,
we need to do this before starting the thread
if non-deamon terminated then deamon also terminate eg ; after exam everthing is over(normal) for family and teacher 

isDaemon: check thread is deamon or not
**Main Thread is non-deamon thread
** other thread depend on their parent  deamon nature eg:if parent deamon then child also deamon or vice versa
** make supportive thread  deamon and other non-deamon (who want support)


files
text file: normal txt file(python decode then show the data)
binary file: stored data in binary format eg: image,vdo,txt..

f=open('filename.txt',mode=r)
f.tell() : return the pointer position
f.seek(integer): move pointer one place to another place from begining 0 to integer
with() : used to open file but no need to close file separatly(explicitly)
pickling: convert class object into  byte stream(we use this for secure data)
  dump(): used to perform pickling

Unpickling: reverse of pickling   byte steam to class object
** for storing structured data in file and perform calculation we use pickling and Unpickling

Directory
os.mkdir('Mydir')   : create new directory
os.makedirs('parentDir/childDir/grandDir')  : create directory hierarchy   
os.chdir('Mydir') : chnage the directory
os.rename('Mydir','YourDir')  : change dir name
os.rmdir('abbcd')  : delete directory 
os.removedirs('ddf/dff/ew')  : delete directories
walk(path,topdown=True,onerror=None): return the content of directory,return object

