Exception : it is a error and that can be handle by programmer
types
1 Built in Exception
2 User Defiend /Custom Exception

all excpetion are represented as a class in python
eg: SyntaxError,ImportError,RunTimeError,....

**if will not handle exception then program can terminate(means stop) or currupt or dataloss

try: block of code in which exception can occur
except: catch an exception raised by try block(try block se jo exception milta h usko handle krte h)
else : if no exception occur (optional)
finally: this block will run irrespective whether there is exception or not (if finally likh h then run hoga, exception ho ya na ho )
synatx:
try:
  statement
except ExceptionName:
  statement 
else :
  statement
finally:
  statement

** we can write multiple exception block

User Defiend Exception : created by programmer
 1.create own exception class using built in exception class as base class
 2.Raising Exception
 3.Handle Exception
synatx :
1>
class MyException(Exception):
    pass(statement)
2>
raise MyException('message')
3>
using try and except block we can handle


exception : programmer can handle and all exception run only run time
error: an exception which can not be handled by programmer then became error and error can occur at compile or run time





Assert statement: used to ensure given condition is True
  * if condition False then exception by name AssertionError is raised along with me message
  * if message not given and condition False then also AssertionError is raised without message
synatx : assert condition,error_message  


Logging: useful to track the error or exception,also helpes in debugging (Log file)
 need to use login Module
 synatx : import logging
basicConfig(**kwargs)  //key values number of arguments  
synatx : basicConfig(**kwargs)
    filename : create file
    filemode: open the file name in append mode('a')
    level:DEBUG,INFO,WARNING,ERROR,CRITICAL
    format: can format the log  (for formatting we can use any format method)
    style: message style

getLogger('abcd'): return logger(logs) with the specified name if anem none then return root logger of the hierarchy
info(msg): this will log a message with level INFO    
warning(msg):this will log a message with level WARNING 
error(msg):this will log a message with level ERROR 
critical(msg):this will log a message with level CRITICAL 
exception(msg):this will log a message with level ERROR 

** low level logs will not display if level is high

**Help**
in cmd :help() : type any module  or any thing it will gives related result
