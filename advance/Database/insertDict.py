from connect import Connection  
conn=Connection()
sql="INSERT INTO students (stu_name,fees) Values(%(name)s,%(fees)s)"
params={"name":"Pramodd","fees":415.23}  #single dictionary
params2=[{"name":"Mansi","fees":3456.23},{"name":"Utkarsh","fees":767.23}]  
myc=conn.cursor()
try:
    #myc.execute(sql,params) # for single
    myc.executemany(sql,params2) # for multiple insert
    conn.commit()
    print("Inserted Successfully")
    print("Affeted Row :",myc.rowcount)
    print("Student Id :",myc.lastrowid)
except: 
    conn.rollback()
    print("Unable to insert")
myc.close()