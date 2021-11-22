from connect import Connection  
conn=Connection()
sql="INSERT INTO students (stu_name,fees) Values(%(name)s,%(fees)s)"
name=input("Enter Name : ")
fees=float(input("Enter fees : "))
params={"fees":fees,"name":name}  #single dictionary
 
myc=conn.cursor()
try:
    myc.execute(sql,params) # for single
    conn.commit()
    print("Inserted Successfully")
    print("Affeted Row :",myc.rowcount)
    print("Student Id :",myc.lastrowid)
except: 
    conn.rollback()
    print("Unable to insert")
myc.close()