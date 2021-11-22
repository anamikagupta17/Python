from connect import Connection  
conn=Connection()
sql="INSERT INTO students (stu_name,fees) Values(%s,%s)" # OR WE CAN USE ? IN PLACE OF %s
name=input("Enter Name : ")
fees=float(input("Enter fees : "))
params=(name,fees)  #single dictionary
myc=conn.cursor(prepared=True)
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