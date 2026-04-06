import mysql.connector as conn

mydb = conn.connect(host = "localhost", user = "root", passwd = "12345")
cursor = mydb.cursor()
cursor.execute("select employe_id, emp_mailid from wasiq.ineuron1")
# for i in cursor.fetchall():
#     print(i)

l = []
for i in cursor.fetchall():
    l.append(i)

print(l)
print(type(l[0]))







