
import sqlite3, csv
conn = sqlite3.connect("agreements.db", check_same_thread=False)
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS applicants(
id INTEGER PRIMARY KEY AUTOINCREMENT,
telegram_id TEXT,
username TEXT,
recruiter TEXT,
full_name TEXT,
passport TEXT,
nationality TEXT,
start_date TEXT,
agreed INTEGER DEFAULT 0,
agree_time TEXT)''')
conn.commit()

def add(data):
    cur.execute('''INSERT INTO applicants
    (telegram_id,username,recruiter,full_name,passport,nationality,start_date)
    VALUES (?,?,?,?,?,?,?)''',
    (data["telegram_id"],data["username"],data["recruiter"],data["full_name"],
     data["passport"],data["nationality"],data["start_date"]))
    conn.commit()

def agree(uid, t):
    cur.execute("UPDATE applicants SET agreed=1, agree_time=? WHERE telegram_id=?", (t, uid))
    conn.commit()

def export_csv(path="applicants.csv"):
    rows = cur.execute("SELECT * FROM applicants").fetchall()
    with open(path,"w",newline="",encoding="utf-8") as f:
        w=csv.writer(f); w.writerow(["id","telegram_id","username","recruiter","full_name","passport","nationality","start_date","agreed","agree_time"])
        w.writerows(rows)
    return path
