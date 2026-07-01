import psycopg
import matplotlib.pyplot as plt

conn = psycopg.connect(
    dbname="analysis",
    user="postgres",
    password="Duluth/77",
    host="localhost",
)

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
