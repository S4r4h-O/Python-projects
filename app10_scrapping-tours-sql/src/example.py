import sqlite3

# Estabilish a connection and cursor
connection = sqlite3.connect("database.db")
cursor = connection.cursor()

# Query data
cursor.execute("SELECT * FROM events WHERE date='2088.10.15'")
rows = (cursor.fetchall())
print(rows)

cursor.execute("SELECT band, date FROM events WHERE date='2088.10.15'")
rows = (cursor.fetchall())
print(rows)

# Insert new rows
# new_rows = [("Cats", "Cat City", "2050.06.21"), 
            # ("Moneky", "Monkey City", "2050.07.09")]

# cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
# connection.commit()

cursor.execute("SELECT * FROM events")
rows = (cursor.fetchall())
print(rows)
