import mysql.connector
try:
    conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="python"
    )
    if(conn.is_connected()):
        print("DB Connected")
except:
    print("Unable to connect")    

#sql="CREATE table students(stu_id INT AUTO_INCREMENT PRIMARY KEY,stu_name VARCHAR(20),fees FLOAT)"
sql="SHOW TABLES"
myc=conn.cursor()
myc.execute(sql)
for i in myc:
    print(i)
myc.close()
conn.close()    