import psycopg2

# importacion 

conexion=psycopg2.connect(user='postgres',
                          password='turnbullac',
                          host='127.0.0.1',
                          port='5432',
                          database='db_personas')

# utilizar cursor
cursor=conexion.cursor()

# sentecnia sql
sql= 'UPDATE personas SET nombre=%s,apellido=%s,edad=%s WHERE idpersona=%s'

# consulta de datos a usuario
idpersona=input('ingrese id de la persona a editar: ')
nombre=input('ingrese nombre: ')
apellido=input('ingrese apellido: ')
edad=input('ingrese edad: ')

#recoleccion de datos
datos=(nombre,apellido,edad,idpersona)

# utilizar el metodo execute
cursor.execute(sql,datos)

# guardar modificacion
conexion.commit()

#contar el numero de cambios
actualizacion=cursor.rowcount

# mostrar mensaje al usuraio
print(f'registro actualizado: {actualizacion}')

# cerrar conexiones
cursor.close()
conexion.close()