import sqlite3
conn = sqlite3.connect(":memory:")

try:
    conn.execute("SELECT * FROM products")
    print("Query successful")
except sqlite3.Error as e:
    print("Database error handled:", e)
finally:
    conn.close()
