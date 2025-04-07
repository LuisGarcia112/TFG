import pandas as pd
import os

# Nombre del archivo CSV de entrada
nombre_archivo = "Analisis.csv"  

# Cargar el archivo CSV sin errores de tipos
df = pd.read_csv(nombre_archivo, low_memory=False)

# Filtrar datos
pc_df = df[df["Base_escan"] == "PC"]
smartphone_df = df[df["Base_escan"] == "SMARTPHONE"]

# Rutas donde se guardarán los archivos
ruta_pc = "C:/Users/Usuario/Desktop/Universidad/QUINTO/TFG/TFG/PC/Datos_PC.csv"
ruta_smartphone = "C:/Users/Usuario/Desktop/Universidad/QUINTO/TFG/TFG/SMARTPHONE/Datos_SMARTPHONE.csv"
# Guardar los archivos filtrados en las rutas especificadas
pc_df.to_csv(ruta_pc, index=False)
smartphone_df.to_csv(ruta_smartphone, index=False)

print(f"Filas con PC: {len(pc_df)}")
print(f"Filas con SMARTPHONE: {len(smartphone_df)}")

print("Archivos guardados correctamente en las rutas especificadas.")
