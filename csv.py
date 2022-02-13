import sqlite3 as db
import os

with open ('AU_DigitalVideo_MM.csv') as f:
    for matn in f:
        matn

conn = db.connect('My_Database.db')
c = conn.cursor()
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

conn.commit()
conn.close()