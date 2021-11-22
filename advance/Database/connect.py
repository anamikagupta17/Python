import mysql.connector
def Connection():
    return mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="python"
    )


