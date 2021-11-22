#database
connect(): used to make connection 
is_connected() : check connection or not return True if connect
close(): close the connection 

cursor(): used for calling execute() method
synatx: cursor_object=connection_object.cursor()
buffered=True : fetch all rows  and return alone buffered object  or combiation of tuple,dictionary..
prepared=True :

execute() : used to execute sql queries
synatx: cursor_object.execute(sql,param=None,multi=False)
 sql : sql query
 param: parameter for the operation in query
 multi: return iterator if True
close() : also used to close cursor
rowcount: give count of rows
lastrowid:while inserting  gives autoimcrment id of tables if multiple records inserting then will give first inserted record id
commit(): save data into db aftter inserting and updating
executemany(): for multiple insert together

parameterized () : %s ,%(key)s 
prepare statement() : fast performance,when repeated statement $s or ?, functionality same as parameterized 
syntax: myc=connection_object.cursor(prepared=True)