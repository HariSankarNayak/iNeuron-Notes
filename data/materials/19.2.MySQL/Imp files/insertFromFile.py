import mysql.connector as connection
import pandas as pandas
import csv

try:
    mydb = connection.connect(host="localhost", user="root", passwd="mysql",use_pure=True)
    #check if the connection is established
    print(mydb.is_connected())
    #create a new database
    query = "Create database GlassData;"
    cursor = mydb.cursor() #create a cursor to execute queries
    cursor.execute(query)
    print("Database Created!!")
    mydb.close() #close the connection

    #Establish a new connection to the database created above
    mydb = connection.connect(host="localhost", database = 'GlassData',user="root", passwd="mysql", use_pure=True)

    #create a new table to store glass data
    query = "CREATE TABLE IF NOT EXISTS GlassData (Index_Number INT(10),RI float(10,5), Na float(10,5), Mg float(10,5),Al float(10,5)," \
            " Si float(10,5), K float(10,5), Ca float(10,5), Ba float(10,5), Fe float(10,5), Class INT(5))"
    cursor = mydb.cursor()  # create a cursor to execute queries
    cursor.execute(query)
    print("Table Created!!")

    #read from the file
    with open('glass.data', "r") as f:
        next(f)
        glass_data = csv.reader(f, delimiter="\n")
        for line in enumerate(glass_data):
            for list_ in (line[1]):
                cursor.execute('INSERT INTO GlassData values ({values})'.format(values=(list_)))
    print("Values inserted!!")
    mydb.commit()
    cursor.close()
    mydb.close()

except Exception as e:
    #mydb.close()
    print(str(e))