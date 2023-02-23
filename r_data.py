from getting_credentials import get
import psycopg2
import pandas as pd

data = get()

conn = psycopg2.connect(
   database=data[2], user=data[0], password=data[1], host='127.0.0.1', port= '5432'
)

conn.autocommit = True
cursor = conn.cursor()

cursor.execute("select * from keywords;")
result_tvn = cursor.fetchall()

pd.options.display.max_colwidth = 100



import json
 
dic = [0 for i in result_tvn]

for j,i in enumerate(result_tvn):
   

   dictionary = {
      "headline": i[0],
      "first_cell": i[1],
      "second_cell": i[2],
      "other_words": i[3]
   }
   
   dic[j] = dictionary


json_object = json.dumps(dic, indent=4 , ensure_ascii=False)
 

with open("/media/pi/KINGSTON/api/key_words2.json", "w") as outfile:
   outfile.write(json_object)