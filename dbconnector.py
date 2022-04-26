import sqlite3
con = sqlite3.connect('rawdata.db')
cur1 = con.cursor()

def init():
    cur1.execute('''CREATE TABLE if not exists rawdata(key text, raw text) ''')

def getKey(key):
    con = sqlite3.connect('rawdata.db')
    cur = con.cursor()
    cur.execute("select * from rawdata where key = '%s'"%(key))
    res = cur.fetchall()
    cur.close()
    con.close()
    for i in res:
        return i[1]
    return ''

def saveKey(key, value):
    con = sqlite3.connect('rawdata.db')
    cur = con.cursor()
    sql1 = "insert into rawdata values  ('%s', '%s')"%(key, value)
    cur.execute(sql1)
    con.commit()
    con.close()
    return True



init()