from packages import *
import sqlite3 as sql
# import sqlite3 as sql

# conn = sql.connect("Password.db")
# c = conn.cursor()
f = True

while f:
    print('''Enter the option number you wish to choose:
             1.Add New userName and password
             2.Edit existing password
             3.
             4.This is option 4
             5.Exit!''')
    n = int(input("Your Option choice: "))
    if n == 1:
        while True:
            uName,password = input("Enter userName and password:").split()
            addVal(uName,password)
            x = input("Do you wish to continue?")
            no = ['n','no','end','nope','nah']
            if x.lower() not in no:
                break
            
    break
