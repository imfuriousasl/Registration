import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS mothers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
               age INTEGER NOT NULL,
               phone TEXT NOT NULL,
                address TEXT,
               weeks_pregnant INTEGER NOT NULL,
               expected_delivery text NOT NULL,
               registration_date TEXT
               notes TEXT
)''')

conn.commit()
conn.close()
print("Database and table created successfully.")
            