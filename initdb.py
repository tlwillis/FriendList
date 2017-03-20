import sqlite3

connection = sqlite3.connect('database.db')
print ('We\'re connected up yo')

connection.execute('CREATE TABLE friends (name TEXT, age INTEGER) ')
print ('Table Created')

connection.close()