import mysql.connector as connection

try:
    mydb = connection.connect(host="localhost", database = 'Student',user="root", passwd="mysql",use_pure=True)
    # check if the connection is established
    print(mydb.is_connected())

    query = "CREATE TABLE StudentDetails (Studentid INT(10) AUTO_INCREMENT PRIMARY KEY,FirstName VARCHAR(60)," \
            "LastName VARCHAR(60), RegistrationDate DATE,Class Varchar(20), Section Varchar(10))"

    cursor = mydb.cursor() #create a cursor to execute queries
    cursor.execute(query)
    print("Table Created!!")
    mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))