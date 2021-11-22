from connect import Connection  
conn=Connection()
sql="delete from students  where stu_id=5"
myc=conn.cursor()
myc.execute(sql)
print("Affeted Row :",myc.rowcount)
myc.close()