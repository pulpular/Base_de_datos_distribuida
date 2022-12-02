# importacion del modulo
import psycopg2

#conexion a base de datos
conexion=psycopg2.connect(user='postgres',
                          password='turnbullac',  
                          host='127.0.0.1',
                          port='5432',
                          database='db_personas')

# utilizar cursor
cursor=conexion.cursor()

# crear la sentencia sql
sql='SELECT * FROM personas WHERE idpersona=%s'

# solicitar datos a usuario
idpersona=input('ingrese el id del registro a mostrar: ')

# uso del metodo execute
cursor.execute(sql,idpersona)

# mostrar resultado
registro=cursor.fetchone()

# mostrar en consola o el usuario
print(registro)

# cerrar conexiones
cursor.close()
conexion.close()