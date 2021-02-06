import mysql.connector as mySql

mydb = mySql.connect(
    host="localhost",
    user="root",
    password="root",
    database="map"
)
cursor = mydb.cursor()
cursor.execute("SELECT * FROM cities")
results = cursor.fetchall()
print(results)

