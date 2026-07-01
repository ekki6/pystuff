#simple script to check postgres connection
import json
import psycopg

#replaced below with JSON bit
#conn = psycopg.connect(
#    dbname="analysis",
#    user="postgres",
#    password="Duluth/77",
#    host="localhost",
#)

with open("dbconfig.json") as f:
    config = json.load(f)


conn = psycopg.connect(**config)


with conn.cursor() as cur:
    cur.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
        ORDER BY table_name;
    """)

    print("Connected!\n")
    print("Tables:")
    for (table,) in cur.fetchall():
        print(f"  {table}")

conn.close()
