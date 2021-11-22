import mysql.connector
try:
    con= mysql.connector.connect(
		host="localhost",
		user="root",
		password=""
		)
    if(con.is_connected()):
        print("Connected")
except:
    print('Unable to connect')
    
print("Before Close:",con.is_connected())     
myc=con.cursor()
#sql="CREATE DATABASE python"
sql="SHOW DATABASEs"
myc.execute(sql)
for d in myc:
  print(d)

myc.close()   
con.close()    
print("After Close:",con.is_connected())  