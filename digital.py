import sqlite3 as db
import csv
import tabulate

conn = db.connect('My_Database.db')
c = conn.cursor()
a_file = open("AU_DigitalVideo_MM.csv")
a_file.seek(408)
rows = csv.reader(a_file,delimiter=';')
c.execute(''' CREATE TABLE IF NOT EXISTS Digital_Video(
            Week_Ending int,
            Brand txt,
            Sub_Brand txt,
            Variant txt,
            Website txt,
            Campaign_Name txt,
            Creative txt,
            Copy_Name txt,
            Adss_Type txt,
            Ads_Format txt,
            Platform txt,
            Thematical_Tactical txt,
            SCJ_Sub_Two_New_launch txt,
            Buying_Type txt,
            Views integer,
            Clicks integer,
            Impressions integer,
            Actual_Spending real,
            Spend_In_USD real
                )''')
#c.executemany("INSERT INTO Digital_Video VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", rows)
c.execute("SELECT * FROM Digital_Video WHERE Actual_Spending='1,215'")
print((c.fetchone()))

#conn.commit()
conn.close()