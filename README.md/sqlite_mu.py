import sqlite3

sqliteConnection = sqlite3.connet('first_example.db')
print("database connected")

cursor = sqliteConnection.cursor()
print("database initialized")

sql_raed_quary = "SELECT * FROM emp;"
cursor.execute(sql_raed_quary)
print(cursor.fetchall())

sqliteConnection.close()