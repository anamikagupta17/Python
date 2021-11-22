from connect import Connection  
conn=Connection()
myc=conn.cursor()
sql="INSERT INTO students (stu_name,fees) Values(%s,%s)"
n=int(input("How many Students : "))
for i in range(n):
    name=input("Enter Name :")
    fees=input("Enter Fees :")
    params=(name,fees)
    myc.execute(sql,params)
    conn.commit()
myc.close()

