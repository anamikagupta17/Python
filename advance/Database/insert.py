from connect import Connection  
conn=Connection()
sql="INSERT INTO students (stu_name,fees) Values('Aman',456.28),('Lakshaman',3553.75),('Pm',453.98)"
myc=conn.cursor()
myc.execute(sql)
print("Affeted Row :",myc.rowcount)
print("Student Id :",myc.lastrowid)
myc.close()