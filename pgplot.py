#simple script to check postgres connection

import json
import psycopg
import matplotlib.pyplot as plt

with open("dbconfig.json") as f:
    config = json.load(f)


conn = psycopg.connect(**config)



query = """
SELECT year, month, soybeans_export_value,
    round(
       avg(soybeans_export_value)
            OVER(ORDER BY year, month
                 ROWS BETWEEN 11 PRECEDING AND CURRENT ROW), 0)
       AS twelve_month_avg
FROM us_exports
ORDER BY year, month;
"""

with conn:
    with conn.cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()

monthly = [row[2] for row in rows]
rolling = [row[3] for row in rows]

plt.plot(monthly, label="Monthly Average")
plt.plot(rolling, label="12-Month Rolling Average")

plt.legend()
plt.grid(True)
plt.show()
