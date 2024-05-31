import pandas as pd

def analizar_calidad_datos(df):
    analisis_calidad = {}
    
    for col in df.columns:
        # Cantidad de valores
        cantidad_valores = df[col].count()
        
        # Cantidad y porcentaje de valores válidos
        cantidad_valores_validos = df[col].notnull().sum()
        porcentaje_valores_validos = (cantidad_valores_validos / cantidad_valores) * 100 if cantidad_valores > 0 else 0
        
        # Cantidad y porcentaje de valores distintos
        cantidad_valores_distintos = df[col].nunique()
        porcentaje_valores_distintos = (cantidad_valores_distintos / cantidad_valores) * 100 if cantidad_valores > 0 else 0
        
        # Cantidad y porcentaje de valores vacíos y nulos
        cantidad_valores_vacios = df[col].isna().sum()
        porcentaje_valores_vacios = (cantidad_valores_vacios / cantidad_valores) * 100 if cantidad_valores > 0 else 0
        cantidad_valores_nulos = df[col].isnull().sum()
        porcentaje_valores_nulos = (cantidad_valores_nulos / cantidad_valores) * 100 if cantidad_valores > 0 else 0
        
        # Valor mínimo y máximo, valor promedio y desviación estándar
        if pd.api.types.is_numeric_dtype(df[col]):
            valor_minimo = df[col].min()
            valor_maximo = df[col].max()
            valor_promedio = df[col].mean()
            desviacion_estandar = df[col].std()
        else:
            valor_minimo = None
            valor_maximo = None
            valor_promedio = None
            desviacion_estandar = None
        
        # Cantidad y porcentaje de valores atípicos (para 2 y 3 desviaciones estándar)
        if valor_promedio is not None and desviacion_estandar is not None:
            limite_superior_2std = valor_promedio + 2 * desviacion_estandar
            cantidad_valores_atipicos_2std = df[col][df[col] > limite_superior_2std].count()
            porcentaje_valores_atipicos_2std = (cantidad_valores_atipicos_2std / cantidad_valores) * 100 if cantidad_valores > 0 else 0
            limite_superior_3std = valor_promedio + 3 * desviacion_estandar
            cantidad_valores_atipicos_3std = df[col][df[col] > limite_superior_3std].count()
            porcentaje_valores_atipicos_3std = (cantidad_valores_atipicos_3std / cantidad_valores) * 100 if cantidad_valores > 0 else 0
        else:
            cantidad_valores_atipicos_2std = None
            porcentaje_valores_atipicos_2std = None
            cantidad_valores_atipicos_3std = None
            porcentaje_valores_atipicos_3std = None
        
        # Guardar resultados en el diccionario de análisis de calidad
        analisis_calidad[col] = {
            'Cantidad de Valores': cantidad_valores,
            'Cantidad de Valores Válidos': cantidad_valores_validos,
            'Porcentaje de Valores Válidos': porcentaje_valores_validos,
            'Cantidad de Valores Distintos': cantidad_valores_distintos,
            'Porcentaje de Valores Distintos': porcentaje_valores_distintos,
            'Cantidad de Valores Vacíos': cantidad_valores_vacios,
            'Porcentaje de Valores Vacíos': porcentaje_valores_vacios,
            'Cantidad de Valores Nulos': cantidad_valores_nulos,
            'Porcentaje de Valores Nulos': porcentaje_valores_nulos,
            'Valor Mínimo': valor_minimo,
            'Valor Máximo': valor_maximo,
            'Valor Promedio': valor_promedio,
            'Desviación Estándar': desviacion_estandar,
            'Cantidad de Valores Atípicos (2 Desviaciones Estándar)': cantidad_valores_atipicos_2std,
            'Porcentaje de Valores Atípicos (2 Desviaciones Estándar)': porcentaje_valores_atipicos_2std,
            'Cantidad de Valores Atípicos (3 Desviaciones Estándar)': cantidad_valores_atipicos_3std,
            'Porcentaje de Valores Atípicos (3 Desviaciones Estándar)': porcentaje_valores_atipicos_3std
        }
    
    return analisis_calidad

# Leer datos desde el archivo CSV

ruta_archivo_csv = r'C:\Users\ustdo\Desktop\Escuela\ultimo semestre\Inteligencia Artificial\practica10\house_prices_train.csv'
datos = pd.read_csv(ruta_archivo_csv)

# Realizar análisis de calidad de datos
analisis = analizar_calidad_datos(datos)

# Mostrar resultados
for col, info in analisis.items():
    print(f"Análisis de la columna: {col}")
    print(info)
    print("\n")

# Convertir el diccionario de resultados en un DataFrame
df_resultados = pd.DataFrame.from_dict(analisis, orient='index')

# Guardar el DataFrame en un archivo CSV
ruta_resultados_csv = r'C:\Users\ustdo\Desktop\Escuela\ultimo semestre\Inteligencia Artificial\practica10\Resultados.csv'
df_resultados.to_csv(ruta_resultados_csv)

print(f"Los resultados del análisis de calidad se han guardado en el archivo: {ruta_resultados_csv}")



