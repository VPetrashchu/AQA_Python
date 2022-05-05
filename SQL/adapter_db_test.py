import psycopg2

conn = psycopg2.connect(dbname="postgres", user="postgres", password="Vaska1@90")

cur = conn.cursor()


#cur.execute("CREATE TABLE supervisitors( visitor_id int PRIMARY KEY, first_name varchar, last_name varchar)")
#cur.execute("INSERT INTO supervisitors (visitor_id, first_name, last_name) VALUES (%s, %s, %s)", (1, "Dmytro", "Panasenko"))
cur.execute("INSERT INTO supervisitors (visitor_id, first_name, last_name) VALUES (%s, %s, %s)", (2, "Andriy", "Hnatyuk"))

cur.execute(""" 
            INSERT INTO supervisitors (visitor_id, first_name, last_name)
            VALUES (%(ID)s, %(first_name)s, %(last_name)s);
            """, {'ID': 3, 'first_name': 'Dmytro', 'last_name': 'Tarasenko'})

conn.commit()

cur.execute("SELECT * FROM supervisitors")

one_line = cur.fetchone() # oucome tupple
print(one_line)

full_fetch = cur.fetchall()
for record in full_fetch:
    print(record)
    
#full_fetch[0][0]  1st line, 1st value

conn.commit()

cur.close()
conn.close()