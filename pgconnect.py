import psycopg

conn = psycopg.connect(
    dbname="analysis",          # or whatever database you're using
    user="postgres",
    password="Duluth/77",
    host="localhost",
)

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
