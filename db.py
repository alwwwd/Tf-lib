import sqlite3 as db

def make_list():
    code_and_status = {}
    conn = db.connect('db.sqlite')
    cur = conn.cursor()
    cur.execute("""select code, name, status from apps""")
    
    for code, name, status  in cur.fetchall():
        code_and_status[code] = {
            "code": code,
            "status": status,
            "name": name
            }
    return dict(code_and_status)