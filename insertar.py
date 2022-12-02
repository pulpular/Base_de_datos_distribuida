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

sql= 'INSERT INTO personas (nombre, apellido, edad) VALUES (%s, %s, %s)'

# solicitud de datos
nombre=input('Ingrese el nombre: ')
apellido=input('Ingrese apellido: ')
edad=input('Ingresa edad: ')

# recoleccion de datos
datos=(nombre, apellido, edad)

# metodo execute
cursor.execute(sql,datos)

# guardar registros
conexion.commit()

# registros insertados
registros=cursor.rowcount

# Mensaje
print(f'Registros insertados con exito: {registros}')

# cerrar conexion
cursor.close()
conexion.close()









