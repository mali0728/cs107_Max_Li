# Coder: Krithika Sundararajan, Xiaohan Yang
# Reviewers: Yujie Cai, Max Li
# Sharer: Krithika Sundararajan

import sqlite3

# Init DB and drop the table if already exists
db = sqlite3.connect('test_db.sqlite') # Create a connection to the database
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS candidates") # Convenient in case you want to start over
cursor.execute("PRAGMA foreign_keys=1")

# Create the table
cursor.execute('''CREATE TABLE candidates (
               id INTEGER PRIMARY KEY NOT NULL, 
               first_name TEXT, 
               last_name TEXT, 
               middle_init TEXT, 
               party TEXT NOT NULL)''')
               
db.commit() # Commit changes to the database

# Read the file
text = None
with open('candidates.txt') as f:
    text = f.readlines()

# For each line in the file except the first (header line), insert into DB
for line in text[1:]:
    # We do line[:-1] to remove the newline character
    id_, first_name, last_name, middle_init, party = line[:-1].split("|")
    id = int(id_)
    # print(id_, first_name, last_name, middle_init, party)
    cursor.execute('''INSERT INTO candidates
               (id, first_name, last_name, middle_init, party)
               VALUES (?, ?, ?, ?, ?)''', 
                (id, first_name, last_name, middle_init, party))
    db.commit()

# Demo
cursor.execute("SELECT * FROM candidates WHERE party = 'D'")
all_rows = cursor.fetchall()
print(all_rows)

cursor.execute("SELECT count(*) FROM candidates")
result = cursor.fetchall()
print(result[0])
