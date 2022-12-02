# importacion del modulo
import psycopg2

#conexion a base de datos
conexion=psycopg2.connect(user='postgres',
                          password='admin',  
                          host='127.0.0.1',
                          port='5432',
                          database='db_personas')

# utilizar cursor
cursor=conexion.cursor()

# sentencia squl
sql= 'DELETE FROM personas WHERE idpersonas=%s'

# solicitar datos del usuario
idpersonas=input('ingrese id a eliminar')

# Ejecucion
cursor.execute(sql.idpersonas)

# Guardar cambios
conexion.commit()

# registro eliminado
registro_eliminado=cursor.rowcount

# Mensaje
print(f'registros eliminados: {registro_eliminado}')

# cerrar conexion
cursor.close()
conexion.close()






