import sqlite3
from pathlib import Path
print("Database location:", Path("shop.db").resolve())

conn=sqlite3.connect('shop.db')
conn.execute('''
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    sales INTEGER NOT NULL DEFAULT 0
)
''')
conn.execute('''INSERT INTO products (name,price,sales) VALUES ("Keyboard", 500, 0)''')
conn.execute('''INSERT INTO products (name,price,sales) VALUES ("Mouse", 300, 0)''')
conn.execute('''INSERT INTO products (name,price,sales) VALUES ("Monitor", 1500, 0)''')

conn.commit()
conn.close()