import pandas as pd
from tabulate import tabulate

def leer_metadatos_csv(ruta_archivo):
    # Leer el archivo CSV
    try:
        df = pd.read_csv(ruta_archivo)
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{ruta_archivo}'")
        return None
    
    # Obtener los metadatos
    num_filas, num_columnas = df.shape
    nombres_columnas = list(df.columns)
    tipos_datos = [str(df[col].dtype) for col in df.columns]
    
    # Crear tabla de metadatos
    tabla_metadatos = [
        ['Número de Filas', num_filas],
        ['Número de Columnas', num_columnas],
        ['Nombres de Columnas', ', '.join(nombres_columnas)],
        ['Tipos de Datos', ', '.join(tipos_datos)]
    ]
    
    return tabla_metadatos

ruta_archivo_csv = r'C:\Users\ustdo\Desktop\Escuela\ultimo semestre\Inteligencia Artificial\practica10\house_prices_train.csv'
metadatos_csv = leer_metadatos_csv(ruta_archivo_csv)

if metadatos_csv:
    print(tabulate(metadatos_csv, headers=['Metadato', 'Valor'], tablefmt='grid'))
