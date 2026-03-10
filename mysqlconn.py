import mysql.connector

conn = mysql.connector.connect(
    host="mysql-service",
    port=3306,
    user="root",
    password="rootpassword",
    database="testdb"
)

cursor = conn.cursor()
cursor.execute("SELECT DATABASE();")
result = cursor.fetchone()

print("Connected to database:", result)

cursor.close()
conn.close()
