from connect import Connection  
conn=Connection()
sql="select * from students"
myc=conn.cursor(buffered=True)
myc.execute(sql)
row=myc.fetchone()
print("one")
print(row)
row1=myc.fetchmany(2)
print("many")
print(row1)
print("all")
row2=myc.fetchall() # it will gives all result except first one becuse first one and limit givien by fetchmany is already fetched 
for i in row2:
    print(i)

myc.close()