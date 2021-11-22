import os
f=open("student.txt",mode='w')
f.write("Hello Anamika ")
lst=['\nAna\n','Parul\n','Pramod\n','Anamika\n']
f.writelines(lst)

f.close()
print(f.readable())
print(f.writable)
print(f.closed)

print("File exist or not")
print(os.path.isfile('student.txt'))
fl=open("student.txt",mode='r')
data=fl.read()
data2=fl.read(5)
print(data)
print(data2)

with open('student.txt') as f3:
    data3=f3.read()
    print(data3)

print("tell and seek method")
p=fl.tell() #return the pointer position from begining
print(p)  
print(fl.seek(4)) #used to move pointer from one position to another position from begining 0-1,0-4...
print(fl.tell()) 

newFile=open('student.txt',mode="r+")  #read and then write
newFile.write("Anamika Python")

newFile=open('ana.txt' ,mode="w+")  #write and then read and overwite data
newFile.write("Anamika Python")

newFile=open('ana.txt' ,mode="w+")  #append and then read 
newFile.write("Anamika Python")


print("copy data from one file to another file")
f1=open('student.txt',mode='r')
f2=open('student1.txt',mode='w')
newdata=f1.read()
f2.write(newdata)