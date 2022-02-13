import sqlite3 as db
import csv
import tabulate

conn = db.connect('My_Database.db')
c = conn.cursor()
a_file = open("AU_DigitalVideo_MM.csv")
a_file.seek(408)
rows = csv.reader(a_file,delimiter=';')
c.execute(''' CREATE TABLE IF NOT EXISTS Digital_Video(
            Week Ending int,
            Brand txt,
            Sub Brand txt,
            Variant txt,
            Website txt,
            Campaign Name txt,
            Creative txt,
            Copy Name txt,
            Adss Type txt,
            Ads Format txt,
            Platform txt,
            Thematical Tactical txt,
            SCJ Sub Two  New launch txt,
            Buying Type txt,
            Views integer,
            Clicks integer,
            Impressions integer,
            Actual Spending integer,
            Spend USD real
                )''')
#c.executemany("INSERT INTO Digital_Video VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", rows)
c.execute("SELECT * FROM Digital_Video")
print((c.fetchmany(1)))


conn.commit()
conn.close()