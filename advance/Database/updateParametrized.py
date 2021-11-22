from connect import Connection  
conn=Connection()
myc=conn.cursor()
sql="Update students set fees=%s where stu_id=%s"  # same for dictionry just add key
fee=input("Enter Fees to update : ")
params={"fees":fee,"id":19}
params=(fee,17)  

try:
    myc.execute(sql,params) 
    conn.commit()
    print("Updated Successfully")
except: 
    conn.rollback()
    print("Unable to Update")
myc.close()