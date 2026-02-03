# `pip install mysql-connector-python`  run this in terminal >> command prompt
import mysql.connector as conn

mydb = conn.connect(host = "localhost", user = "root", passwd = "12345")
print(mydb)
cursor = mydb.cursor()
cursor.execute("create database wasiq") # Create a db named "wasiq"
cursor.execute("show databases")

# s = "create table wasiq.ineuron1(employe_id int(10)  , emp_name varchar(80) , emp_mailid varchar(20),emp_salary int(6) , emp_attendence int(3))"
#cursor.execute(s)

#q2 = cursor.execute("select * from wasiq.ineuron1")
#print(q2)

#print(cursor.fetchall())