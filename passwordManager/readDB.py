import sqlite3 as sql

conn = sql.connect('Expenses.db')
c = conn.cursor()
c.execute('select * from expenses')
for i in c:
    print(i)