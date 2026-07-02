#simple script to check postgres connection

import json
import psycopg
import matplotlib.pyplot as plt

with open("dbconfig.json") as f:
    config = json.load(f)


conn = psycopg.connect(**config)

with open("nyquery.sql") as f:
    query = f.read()

with conn:
    with conn.cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()

hour = [row[0] for row in rows]
trips = [row[1] for row in rows]

plt.plot(hour, trips)
#plt.plot(rolling, label="12-Month Rolling Average")

#plt.legend()
plt.title("taxi trips during a day")
plt.xlabel("hour")
plt.ylabel("trips")

plt.grid(True)
plt.show()
