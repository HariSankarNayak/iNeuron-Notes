import mysql.connector as connection

try:
    mydb = connection.connect(host="localhost", database = 'Student',user="root", passwd="mysql",use_pure=True)
    # check if the connection is established
    print(mydb.is_connected())
    query = "INSERT INTO StudentDetails VALUES ('1132','Sachin','Kumar','1997-11-11','Eleventh','A')"

    cursor = mydb.cursor() #create a cursor to execute queries
    cursor.execute(query)
    print("Values inserted into the table!!")
    mydb.commit()
    mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))