from connect import Connection  
conn=Connection()
sql="UPDATE  students Set fees=546.87 where stu_id=4"
myc=conn.cursor()
myc.execute(sql)
print("Affeted Row :",myc.rowcount)
myc.close()