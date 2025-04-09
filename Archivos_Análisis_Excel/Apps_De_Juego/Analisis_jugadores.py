import pandas as pd

# Cargar el archivo CSV 
ruta_jugadores = "juego_y_escaneo.csv"

# Leer los datos en pandas DataFrames
df_jugadores = pd.read_csv(ruta_jugadores, encoding="utf-8")

# Calcular la media de la edad, ignorando los valores NaN
media_edad = df_jugadores['c2_pcan'].mean()
    
# Imprimir la media de edad
print(f"La media de edad de los usuarios es: {media_edad:.2f}")


# Filtrar las filas donde la columna 'a1_pcan_14' tenga el valor 'sí'
respuestas_si = df_jugadores[df_jugadores["a1_pcan_14"] == "Sí"]

# Imprimir el número de filas que han respondido "sí"
numero_respuestas_si = len(respuestas_si)
print(f"El número de personas que afirman haber utilizado servicios de apuestas o casinos online en los últimos 6 meses es: {numero_respuestas_si} de {len(df_jugadores)}")


# Selección de preguntas relevantes
preguntas = ['i6aan_1', 'i6aan_2', 'i6aan_5', 'i6aan_8', 'i6aan_9', 'i6ban_5', 'i6ban_6', 'i6ban_7']

# Rellenar valores nulos con "NC"
df_jugadores[preguntas] = df_jugadores[preguntas].fillna("NC")

# Mapear respuestas de texto a números
mapeo_respuestas = {
    "Nunca": 1, 
    "Rara vez": 2, 
    "Algunas veces": 3,
    "Bastantes veces": 4, 
    "La mayor parte del tiempo": 5, 
    "NC": 0
}

df_jugadores[preguntas] = df_jugadores[preguntas].applymap(lambda x: mapeo_respuestas.get(str(x).strip(), 0))

# Clasificación basada en reglas
df_jugadores['adicto'] = df_jugadores[preguntas].apply(
    lambda row: 2 if 0 in row.values else 1 if sum(row >= 4) >= 4 else 0,
    axis=1
)

# Imprimir el número de usuarios clasificados en cada categoría
clasificados = df_jugadores['adicto'].value_counts()

# Imprimir el resumen
print("Resumen de clasificación de usuarios:")
print(f"Usuarios clasificados como 'No Adicto' (0): {clasificados.get(0, 0)}")
print(f"Usuarios clasificados como 'Adicto' (1): {clasificados.get(1, 0)}")
print(f"Usuarios clasificados como 'No Contesta' (2): {clasificados.get(2, 0)}")


# Sumar todas las filas de las dos columnas
total_dinero = df_jugadores['d2x_pcan_1'].sum() + df_jugadores['d2x1_pcan_1'].sum()
    
# Contar el número de usuarios (filas)
num_usuarios = len(df_jugadores)
    
# Calcular la pérdida económica promedio por usuario
perdida_media = total_dinero / num_usuarios

# Imprimir el resultado
print(f"La pérdida económica media por usuario es: {perdida_media:.2f} euros.")