from getting_credentials import get
import psycopg2
import json
from configparser import ConfigParser
from datetime import datetime
from calendar import monthrange



t = datetime.now()

date = t.strftime("%Y-%m-%d")
u = f"{t.year}-{t.month}-{t.day}"

eh = 1
day = t.day
month = t.month
year = t.year



data = get()

conn = psycopg2.connect(
   database=data[2], user=data[0], password=data[1], host='127.0.0.1', port= '5432'
)

conn.autocommit = True
cursor = conn.cursor()


def number_of_days_in_month(year=2023, month=2):
    return monthrange(year, month)[1]



# archive update

list_of_objs = [[],[]]

with open("//media/pi/KINGSTON/api/number.json") as f:
    f = json.load(f)
    month = f["number"]

    date = f"{year}-{month}-{int(number_of_days_in_month(year, int(month)))}"
    date2 = f"{year}-{month}-{1}"


cursor.execute(f"select * from main_tvp where date between '{date2}' and '{date}';")
tvp = cursor.fetchall()


cursor.execute(f"select * from main_tvn where date between '{date2}' and '{date}';")
tvn = cursor.fetchall()

for i in tvn:
    list_of_objs[0].append(i[1])

for i in tvp:
    list_of_objs[1].append(i[1])


with open(f"//media/pi/KINGSTON/api/{month}.json", 'w') as f:
    json.dump(list_of_objs, f, ensure_ascii=False)


#Keyword update 
#add_key_to_db.py
import r_data


with open("//media/pi/KINGSTON/api/counter.json") as f:
    f = json.load(f)
    cc= f["counter"]


cc += 1
list_of_objs = {"counter": cc }
with open(f"//media/pi/KINGSTON/api/counter.json", 'w') as f:
    json.dump(list_of_objs, f, ensure_ascii=False)

