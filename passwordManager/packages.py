import sqlite3 as sql
import re

conn = sql.connect('Password.db')
c = conn.cursor()

# c.execute('''Create table passManage (userName text not null, password text not null)''')
# c.execute("insert into passManage values ('Rahul','abc123456')")

def addCol(colName):
    c.execute(f"alter table passManage add column {colName} text not null")

def editPass(userName,newPass):
    if len(newPass)>=8:
        c.execute(f"update passManage set password = '{newPass}' where userName = '{userName}'")
    else:
        print("Password must be 8 characters long")

def searchPass(userName):
    c.execute(f"select password from passManage where userName = '{userName}'")
    for i in c:
        return i[0]
        
def addVal(userName,password):
    c.execute(f"insert into passManage values('{userName}','{password}')")

def removeVal(userName=None,password=None):
    if userName != None:
        c.execute(f"delete from passManage where userName = '{userName}'")
    elif password!=None:
        c.execute(f"delete from passManage where password = '{password}'")

def viewPass():
    c.execute(f"select * from passManage")
    for i in c:
        print(i)

def is_strong_password(password):
    if len(password) < 8:
        return False

    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    special = re.search(r'[^\w\s]', password)

    if not (uppercase and lowercase and digit and special):
        return False

    common_passwords = ['password', '123456', 'qwerty', 'letmein', 'monkey', '111111', 'abc123', 'football']
    if password.lower() in common_passwords:
        return False
    return True
conn.commit()