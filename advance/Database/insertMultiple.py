from connect import Connection  
conn=Connection()
sql="INSERT INTO students (stu_name,fees) Values(%s,%s)"
params=[("pppp",345.67),("dsfsdf",45.67),("fddfh",34.56)]
myc=conn.cursor()
myc.executemany(sql,params)
conn.commit()
print("Affeted Row :",myc.rowcount)
print("Student Id :",myc.lastrowid)
myc.close()