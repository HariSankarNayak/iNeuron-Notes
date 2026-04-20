import mysql.connector as connection

try:
    mydb = connection.connect(host="localhost",user="root", passwd="mysql",use_pure=True)
    # check if the connection is established

    query = "SHOW DATABASES"

    cursor = mydb.cursor() #create a cursor to execute queries
    cursor.execute(query)
    print(cursor.fetchall())

except Exception as e:
    mydb.close()
    print(str(e))