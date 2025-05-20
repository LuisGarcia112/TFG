import pandas as pd

# Cargar los archivos CSV 
ruta_smarthpone = "Datos_SMARTPHONE.csv"

# Leer los datos en pandas DataFrames
df_smartphone = pd.read_csv(ruta_smarthpone, encoding="utf-8")


# Asegurarnos de que los valores estén bien normalizados (sin espacios adicionales)
df_smartphone["b1b_an_4"] = df_smartphone["b1b_an_4"].str.strip()
df_smartphone["Antivirus_AN"] = df_smartphone["Antivirus_AN"].str.strip()

# Combinaciones
cond1 = (df_smartphone["b1b_an_4"] == "Sí") & (df_smartphone["Antivirus_AN"] != "Ninguno")
cond2 = (df_smartphone["b1b_an_4"] == "Sí") & (df_smartphone["Antivirus_AN"] == "Ninguno")
cond3 = (df_smartphone["b1b_an_4"] == "No") & (df_smartphone["Antivirus_AN"] != "Ninguno")
cond4 = (df_smartphone["b1b_an_4"] == "No") & (df_smartphone["Antivirus_AN"] == "Ninguno")
cond5 = df_smartphone["b1b_an_4"].isin(["Ns/Nc"])  

# Conteos
print("Usuarios que dicen que SÍ tienen antivirus y efectivamente tienen uno:", cond1.sum())
print("Usuarios que dicen que SÍ tienen antivirus pero no tienen ninguno:", cond2.sum())
print("Usuarios que dicen que NO tienen antivirus pero sí tienen uno:", cond3.sum())
print("Usuarios que dicen que NO tienen antivirus y no tienen ninguno:", cond4.sum())
print("Usuarios que respondieron Ns/Nc:", cond5.sum())

# Suma total de todos los usuarios considerados en las combinaciones
total = cond1.sum() + cond2.sum() + cond3.sum() + cond4.sum() + cond5.sum()
print("Suma total de todos los usuarios en las combinaciones:", total)
