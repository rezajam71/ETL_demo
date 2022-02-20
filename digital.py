from ctypes.wintypes import POINT
from msilib import Table
from pickletools import read_long1
import sqlite3 as db
import csv
from tabulate import tabulate
#=================================================================================
#==============================OPEN CSV FILE=====================================
#=================================================================================
conn = db.connect('My_Database.db')
c = conn.cursor()
a_file = open("AU_DigitalVideo_MM.csv")
a_file.seek(408)
rows =(csv.reader(a_file,delimiter=';'))
#=================================================================================
#=============================CREATE A TABLE IN DATABASE==========================
#=================================================================================
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

#=================================================================================
#==============================Fill in the columns================================
#=================================================================================
def insert_rows(values):
    with conn:
        c.executemany("INSERT INTO Digital_Video VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", values)
#=================================================================================
#==============================Calling data=======================================
#=================================================================================
def call_by_column(title):
    c.execute(f"SELECT {title} FROM Digital_Video")
    print(tabulate(c.fetchall(),headers=[title],tablefmt='simple'))

def call_all_data():
    c.execute("SELECT *FROM Digital_Video")
    print((c.fetchall()))
#=================================================================================
#==============================DELET data=========================================
#=================================================================================
def delet_values(title,values):
    with conn:
        c.execute(f"DELETE FROM Digital_Video WHERE {title}='{values}'")
#=================================================================================
#==============================UPDATE data========================================
#=================================================================================
def Update_values(title,Old_values,New_Value):
    with conn:
        c.execute(f"UPDATE Digital_Video SET {title}='{New_Value}' WHERE {title}='{Old_values}'")
#=================================================================================
#==============================Replace STR========================================
#=================================================================================
def replace_values(title,Old_Value,New_value):
    with conn:
        c.execute(f"UPDATE Digital_Video SET {title} = REPLACE({title},'{Old_Value}','{New_value}')")
conn.close()

