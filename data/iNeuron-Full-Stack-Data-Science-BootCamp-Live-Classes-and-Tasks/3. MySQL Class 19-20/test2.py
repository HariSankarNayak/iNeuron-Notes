import mysql.connector as conn

mydb = conn.connect(host = "localhost", user = "root", passwd = "12345")
cursor = mydb.cursor()
s = "insert into wasiq.ineuron1 values(1, 'Mohammad Wasiq', 'gl0427@myamu.ac.in', 999999, 999)"
cursor.execute(s)
mydb.commit()

cursor.execute("select * from wasiq.ineuron1")
for i in cursor.fetchall():
    print(i)