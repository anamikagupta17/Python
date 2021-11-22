import os
print(os.getcwd()) # get current directory
#os.mkdir('Mydir')   # create new directory
#os.makedirs('parentDir/childDir/grandDir')  # create directory hierarchy   
#os.chdir('Mydir') # chnage the directory
#os.rename('Mydir','YourDir')  # change dir name
#os.rmdir('YourDir')  # delete directory 

w=os.walk('parentDir') # dot cueent directory
for i in w:
    print(i)

