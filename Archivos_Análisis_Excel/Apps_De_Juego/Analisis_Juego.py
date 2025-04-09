import pandas as pd

# Cargar los archivos CSV 
ruta_juego = "juego.csv"
ruta_sin_filtrar = "Analisis.csv"

# Leer los datos en pandas DataFrames
df_juego = pd.read_csv(ruta_juego, encoding="utf-8")
df_analisis = pd.read_csv(ruta_sin_filtrar, encoding="utf-8")

# Ver cuántos valores de "encuesta" están en "cod_escan"
coinciden = df_analisis["cod_escan"].isin(df_juego["encuesta"])

# Mostrar el total de coincidencias
total_coinciden = coinciden.sum()
print(f"Hay {total_coinciden} usuarios de 'Analisis.csv' que también están en 'juego.csv'.")

print(f"El archivo 'juego.csv' tiene {len(df_juego)} filas en total.")

# Filtrar las filas de df_analisis donde cod_escan coincide con encuesta de df_juego
usuarios_en_analisis = df_analisis[coinciden]

# Guardar esas filas en un nuevo CSV
usuarios_en_analisis.to_csv("juego_y_escaneo.csv", index=False, encoding="utf-8")

print("Se ha creado el archivo 'juego_y_escaneo.csv' con las filas de 'Analisis.csv' que coinciden.")

