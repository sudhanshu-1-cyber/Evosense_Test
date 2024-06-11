import sqlite3
import csv

con = sqlite3.connect("evo.db")
cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

#query = "INSERT INTO sys_command VALUES(null, 'steam', 'C:\\Program Files (x86)\\Steam\\steam.exe')"
#cursor.execute(query)
#con.commit()

#query = "DELETE FROM sys_command WHERE id = 2 "
#cursor.execute(query)
#con.commit()

#query = "UPDATE sys_command SET id = 3 WHERE id = 4"
#cursor.execute(query)
#con.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

#query = "INSERT INTO web_command VALUES(null, 'gemini', 'https://gemini.google.com/')"
#cursor.execute(query)
#con.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS contacts(id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

#Specifying the column to import
#desired_columns_indices=[0,33]

# Read data from csv and insert into SQLite table for desired column
#with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#    csvreader = csv.reader(csvfile)
#    for row in csvreader:
#        selected_data = [row[i] for i in desired_columns_indices]
#        cursor.execute('''INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

#commit changes and close connection
#con.commit()
#con.close()

#query = 'sachin'
#query = query.strip().lower()

#cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
#results = cursor.fetchall()
#print(results[0][0])

#cursor.execute('''UPDATE contacts SET name = "Ankit Joshi" WHERE id = 38''')
#con.commit()