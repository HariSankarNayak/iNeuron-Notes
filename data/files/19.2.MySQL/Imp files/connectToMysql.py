import mysql.connector as connection

try:
    mydb = connection.connect(host="localhost", user="root", passwd="mysql",use_pure=True)
    # check if the connection is established
    print(mydb.is_connected())
    mydb.close()
except Exception as e:
    print(str(e))