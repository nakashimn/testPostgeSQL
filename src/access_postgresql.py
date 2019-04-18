import os
import sys
import glob
import numpy as np
import pandas as pd
import psycopg2


dsn = os.environ.get("DATABASE_URL")

conn = psycopg2.connect(host="localhost",
                        database="test",
                        user="nakashimn",
                        password="luplun0122")

cursor = conn.cursor()

member = ["Tae", "Sakura", "Saki", "Ai", "Junko", "Yuugiri", "Lily"]

for i in range(7):
    sql = "insert into flanshsh values('{}', '{}')".format(i, member[i])
    cursor.execute(sql)

conn.commit()

cursor.close()
conn.close()
