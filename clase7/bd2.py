#ejemplo de conexion a postgresql con psycopg2
import psycopg2
import os

os.system('cls')

conn = psycopg2.connect("dbname=python_intermedio_db user=postgres password=S3S3Sp22*")

#Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute("SELECT * FROM usuarios WHERE id = 50;")
print(cur.fetchone())

print('-' * 70)

cur.execute("SELECT * FROM usuarios;")
#print(cur.fetchall())
usuarios = cur.fetchall()

for usuario in usuarios:
    print(usuario)

#Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()