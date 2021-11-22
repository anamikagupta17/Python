from connect import Connection  
def insert_student(name,fees):
    conn=Connection()
    sql="INSERT INTO students (stu_name,fees) Values(%(name)s,%(fees)s)"
    params={"fees":fees,"name":name}  #single dictionary
    myc=conn.cursor()
    try:
        myc.execute(sql,params) # for single
        conn.commit()
        print("Student Id :",myc.lastrowid)
    except: 
        conn.rollback()
        print("Unable to insert")
    myc.close()

while True:
    name=input("Enter Name : ")
    fees=float(input("Enter fees : "))    
    insert_student(name,fees)
    ans=input("Do you want to exist y/n?")
    if(ans=="y"):
        break
