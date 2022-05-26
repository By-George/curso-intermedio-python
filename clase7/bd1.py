#ejemplo de conexion a postgresql con psycopg2
import psycopg2

conn = psycopg2.connect("dbname=python_intermedio_db user=postgres password=S3S3Sp22*")

#Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute("SELECT * FROM usuarios;")
print(cur.fetchone())

Make the changes to the database persistent
>>> conn.commit()

# Close communication with the database
cur.close()
conn.close()