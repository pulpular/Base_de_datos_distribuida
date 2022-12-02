import psycopg2

# importacion 

conexion=psycopg2.connect(user='postgres',
                          password='turnbullac',
                          host='127.0.0.1',
                          port='5432',
                          database='db_personas')

# utilizar cursor
cursor=conexion.cursor()

# sentencia sql
sql='SELECT * FROM personas'

# ejecucion
cursor.execute(sql)

# muestra
registro=cursor.fetchall()
print(registro)

# cerrar secion

cursor.close()
conexion.close()