import psycopg2, time, os

DB_HOST = os.getenv('DB_HOST', 'debby') 
DB_USER = os.getenv('DB_USER', 'user')
DB_PASS = os.getenv('DB_PASS', 'pass')
DB_NAME = os.getenv('DB_NAME', 'appdb')

print("🔄 Ethan is starting... trying to remember what is missing...")
conn = None
while conn is None:
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST
        )
    except Exception:
        print("Waiting for Debby to be ready...")
        time.sleep(2)

cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS items (id SERIAL PRIMARY KEY, name TEXT);")
cur.execute("INSERT INTO items (name) VALUES ('Cheese'), ('Flour'), ('Yeast'), ('Tomatoes');")
conn.commit()
cur.close()
conn.close()
print("Ethan succesfully populated data!")
