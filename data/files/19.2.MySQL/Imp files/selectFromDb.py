import mysql.connector as connection


try:
    mydb = connection.connect(host="localhost", database = 'GlassData',user="root", passwd="mysql",use_pure=True)
    #check if the connection is established
    print(mydb.is_connected())
    query = "Select * from GlassData;"
    cursor = mydb.cursor() #create a cursor to execute queries
    cursor.execute(query)
    for result in cursor.fetchall():
        print(result)
    mydb.close() #close the connection


except Exception as e:
    #mydb.close()
    print(str(e))