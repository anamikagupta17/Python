from connect import Connection  
conn=Connection()
myc=conn.cursor()
#sql="delete from students where stu_id=%s"
#params=(3,)  #single tuple
sql="delete from students where stu_id=%(id)s"
params={"id":15}  #for dictionary

try:
    myc.execute(sql,params) # for single
    conn.commit()
    print("Deleted Successfully")
except: 
    conn.rollback()
    print("Unable to Delete")
myc.close()