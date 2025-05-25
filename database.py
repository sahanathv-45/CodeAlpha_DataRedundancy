import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (name TEXT, email TEXT)''')
conn.commit()
conn.close()

print("Database and table created successfully!")


