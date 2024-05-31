import pymysql
from pymysql import Error

def extraer_metadatos(host, puerto, esquema, usuario, contraseña):
    """
    Extrae metadatos de una base de datos MySQL.

    Parámetros:
        host (str): El nombre de host del servidor MySQL.
        puerto (int): El número de puerto del servidor MySQL.
        esquema (str): El nombre del esquema de la base de datos de la que se extraerán los metadatos.
        usuario (str): El nombre de usuario de la cuenta de MySQL que se utilizará para conectarse a la base de datos.
        contraseña (str): La contraseña de la cuenta de MySQL que se utilizará para conectarse a la base de datos.
    """

    try:
        # Establecer conexión a la base de datos
        conexion = pymysql.connect(
            host=host,
            port=puerto,
            database=esquema,
            user=usuario,
            password=contraseña
        )

        # Crear un cursor para ejecutar consultas
        cursor = conexion.cursor()

        # Extraer metadatos del gestor de la base de datos
        cursor.execute("SELECT @@version")
        gestor_version = cursor.fetchone()[0]
        print("Gestor de la base de datos:")
        print("Nombre:", "MySQL")
        print("Versión:", gestor_version)

        # Extraer metadatos de la base de datos
        cursor.execute("SELECT DATABASE()")
        nombre_base_datos = cursor.fetchone()[0]
        print("\nBase de datos:")
        print("Nombre:", nombre_base_datos)
        print("Descripción:", "Descripción de la base de datos")  
        print("Propietario:", "Propietario de la base de datos") 
        cursor.execute("SELECT DATABASE()")
        fecha_creacion = cursor.fetchone()[0]
        print("Fecha de creación:", fecha_creacion)
        cursor.execute("SELECT DATABASE()")
        fecha_modificacion = cursor.fetchone()[0]
        print("Fecha de última modificación:", fecha_modificacion)
        cursor.execute("SELECT DATABASE()")
        tamaño = cursor.fetchone()[0]
        print("Tamaño:", tamaño)
        cursor.execute("SELECT DATABASE()")
        ubicacion_fisica = cursor.fetchone()[0]
        print("Ubicación física:", ubicacion_fisica)
        cursor.execute("SELECT DATABASE()")
        motor_almacenamiento = cursor.fetchone()[0]
        print("Motor de almacenamiento:", motor_almacenamiento)
        cursor.execute("SELECT DATABASE()")
        conjunto_caracteres = cursor.fetchone()[0]
        print("Conjunto de caracteres:", conjunto_caracteres)
        cursor.execute("SELECT DATABASE()")
        codificacion_caracteres = cursor.fetchone()[0]
        print("Codificación de caracteres:", codificacion_caracteres)

        # Extraer metadatos de las tablas
        cursor.execute("SHOW TABLES")
        tablas = cursor.fetchall()
        for tabla in tablas:
            nombre_tabla = tabla[0]
            print("\nTabla:", nombre_tabla)
            print("Descripción:", "Descripción de la tabla")  
            print("Tipo:", "Tipo de tabla") 
            cursor.execute(f"SELECT CREATE_TIME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{nombre_tabla}'")
            fecha_creacion = cursor.fetchone()[0]
            print("Fecha de creación:", fecha_creacion)
            cursor.execute(f"SELECT UPDATE_TIME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{nombre_tabla}'")
            fecha_modificacion = cursor.fetchone()[0]
            print("Fecha de última modificación:", fecha_modificacion)
            cursor.execute(f"SELECT TABLE_ROWS FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{nombre_tabla}'")
            numero_filas = cursor.fetchone()[0]
            print("Número de filas:", numero_filas)
            cursor.execute(f"SELECT COUNT(COLUMN_NAME) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{nombre_tabla}'")
            numero_columnas = cursor.fetchone()[0]
            print("Número de columnas:", numero_columnas)
            
            # Extraer metadatos de las columnas de la tabla
            cursor.execute(f"DESCRIBE {nombre_tabla}")
            columnas = cursor.fetchall()
            for columna in columnas:
                nombre_columna = columna[0]
                tipo_columna = columna[1]
                posicion_columna = columna[3]
                valor_defecto = columna[4]
                print("Columna:", nombre_columna)
                print("Tipo:", tipo_columna)
                print("Posición en tabla:", posicion_columna)
                print("Valor por defecto:", valor_defecto)
                
        # Cerrar el cursor y la conexión
        cursor.close()
        conexion.close()

    except Error as e:
        print("Error al conectar a la base de datos:", e)

# Valores predeterminados para los parámetros de conexión
host = "localhost"
puerto = 3306  # Puerto predeterminado para MySQL
esquema = "sueldos"
usuario = "root"
contraseña = "localhost"  

# Llamada a la función con los valores predeterminados
extraer_metadatos(host, puerto, esquema, usuario, contraseña)
