import sqlite3

conn = sqlite3.connect("boxers.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM boxers")
rows = cursor.fetchall()

print("Имя\tВозраст\tРекорд")
print("-" * 30)
for row in rows:
    print(f"{row[0]}\t{row[1]}\t{row[2]}")

conn.close()
