import mysql.connector
# addded comment
conn = mysql.connector.connect(
    host="mysql-service",
    port=3306,
    user="root",
    #password="rootpassword",
    password ="MySQL@123"
    database="mysqldb"
)

cursor = conn.cursor()
cursor.execute("SELECT DATABASE();")
result = cursor.fetchone()

print("Connected to database:", result)

cursor.close()
conn.close()
