import sqlite3

conn = sqlite3.connect('mycampushub.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS facultys (
        username TEXT,
        password TEXT,
        names TEXT,
        department TEXT,
        designation TEXT,
        mobile INTEGER,
        email TEXT,
        specification TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        username TEXT,
        password TEXT,
        name TEXT,
        fathername TEXT,
        mothername TEXT,
        mobilenumber INTEGER,
        email TEXT,
        course TEXT,
        address TEXT,
        intermarks INTEGER,
        aadharnumber INTEGER
    )
''')
conn.commit()
conn.close()
