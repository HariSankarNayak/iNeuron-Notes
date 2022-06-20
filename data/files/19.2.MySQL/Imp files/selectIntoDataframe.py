import mysql.connector as connection
import pandas as pandas

try:

    mydb = connection.connect(host="localhost", database='GlassData', user="root", passwd="mysql", use_pure=True)
    # check if the connection is established
    print(mydb.is_connected())
    query = "Select * from GlassData;"
    result_dataFrame = pandas.read_sql(query,mydb)
    print(result_dataFrame)

    mydb.close()  # close the connection

except Exception as e:
    #mydb.close()
    print(str(e))