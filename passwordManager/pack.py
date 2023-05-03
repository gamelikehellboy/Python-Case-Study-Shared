import sqlite3 as sql
conn = sql.connect('Password.db')
c = conn.cursor()
class Passmanager:
    userName = ""
    password = ""

    def addcol(colName):
        c.execute(f"alter table passManage add column {colName} text")
        conn.commit()
    
    def addVal(userName,password):
        c.execute(f"insert into passManage values ('{userName}','{password}')")
        conn.commit()
    def removeCol(colName):
        c.execute(f"alter table passManage drop column '{colName}'")
        conn.commit()
    def editPass(userName,newPass):
        c.execute(f"update passManage set password = '{newPass}' where userName = '{userName}'")
        conn.commit()