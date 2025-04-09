import pandas as pd

# Cargar los archivos CSV 
ruta_pc = "Datos_PC.csv"

# Leer los datos en pandas DataFrames
df_pc = pd.read_csv(ruta_pc, encoding="utf-8")


# Asegurarnos de que los valores estén bien normalizados (sin espacios adicionales)
df_pc["b1_pc_1"] = df_pc["b1_pc_1"].str.strip()
df_pc["Antivirus_PC"] = df_pc["Antivirus_PC"].str.strip()

# Combinaciones
cond1 = (df_pc["b1_pc_1"] == "Sí") & (df_pc["Antivirus_PC"] != "Ninguno")
cond2 = (df_pc["b1_pc_1"] == "Sí") & (df_pc["Antivirus_PC"] == "Ninguno")
cond3 = (df_pc["b1_pc_1"] == "0.0") & (df_pc["Antivirus_PC"] != "Ninguno")
cond4 = (df_pc["b1_pc_1"] == "0.0") & (df_pc["Antivirus_PC"] == "Ninguno")
cond5 = df_pc["b1_pc_1"].isin(["Ns/Nc"])  

# Conteos
print("\n--- Análisis de ANTIVIRUS ---")
print("Usuarios que dicen que SÍ tienen antivirus y efectivamente tienen uno:", cond1.sum())
print("Usuarios que dicen que SÍ tienen antivirus pero no tienen ninguno:", cond2.sum())
print("Usuarios que dicen que NO tienen antivirus pero sí tienen uno:", cond3.sum())
print("Usuarios que dicen que NO tienen antivirus y no tienen ninguno:", cond4.sum())
print("Usuarios que respondieron Ns/Nc:", cond5.sum())

# Suma total de todos los usuarios considerados en las combinaciones
total = cond1.sum() + cond2.sum() + cond3.sum() + cond4.sum() + cond5.sum()
print("Suma total de todos los usuarios en las combinaciones:", total)


# Asegurarnos de que los valores estén bien normalizados (sin espacios adicionales)
df_pc["b1_pc_2"] = df_pc["b1_pc_2"].str.strip()
df_pc["Firewal_PC"] = df_pc["Firewal_PC"].str.strip()

# Combinaciones para FIREWALL
f_cond1 = (df_pc["b1_pc_2"] == "Sí") & (df_pc["Firewal_PC"] == "Tiene firewal activo")
f_cond2 = (df_pc["b1_pc_2"] == "Sí") & (df_pc["Firewal_PC"] == "No tiene firewal activo")
f_cond3 = (df_pc["b1_pc_2"] == "0.0") & (df_pc["Firewal_PC"] == "Tiene firewal activo")
f_cond4 = (df_pc["b1_pc_2"] == "0.0") & (df_pc["Firewal_PC"] == "No tiene firewal activo")
f_cond5 = df_pc["b1_pc_2"].isin(["Ns/Nc"])

# Conteos
print("\n--- Análisis de FIREWALL ---")
print("Usuarios que dicen que SÍ tienen firewall y efectivamente lo tienen:", f_cond1.sum())
print("Usuarios que dicen que SÍ tienen firewall pero no lo tienen activo:", f_cond2.sum())
print("Usuarios que dicen que NO tienen firewall pero sí lo tienen activo:", f_cond3.sum())
print("Usuarios que dicen que NO tienen firewall y no lo tienen activo:", f_cond4.sum())
print("Usuarios que respondieron Ns/Nc:", f_cond5.sum())

# Total
f_total = f_cond1.sum() + f_cond2.sum() + f_cond3.sum() + f_cond4.sum() + f_cond5.sum()
print("Suma total de todos los usuarios en las combinaciones de firewall:", f_total)

# Asegurarnos de que los valores estén bien normalizados (sin espacios adicionales)
df_pc["b1_pc_3"] = df_pc["b1_pc_3"].str.strip()
df_pc["Antispam_PC"] = df_pc["Antispam_PC"].str.strip()

# Combinaciones para ANTISPAM
a_cond1 = (df_pc["b1_pc_3"] == "Sí") & (df_pc["Antispam_PC"] == "Tiene")
a_cond2 = (df_pc["b1_pc_3"] == "Sí") & (df_pc["Antispam_PC"] == "No tiene")
a_cond3 = (df_pc["b1_pc_3"] == "0.0") & (df_pc["Antispam_PC"] == "Tiene")
a_cond4 = (df_pc["b1_pc_3"] == "0.0") & (df_pc["Antispam_PC"] == "No tiene")
a_cond5 = df_pc["b1_pc_3"].isin(["Ns/Nc"])

# Conteos
print("\n--- Análisis de ANTISPAM ---")
print("Usuarios que dicen que SÍ tienen antispam y efectivamente lo tienen:", a_cond1.sum())
print("Usuarios que dicen que SÍ tienen antispam pero no lo tienen:", a_cond2.sum())
print("Usuarios que dicen que NO tienen antispam pero sí lo tienen:", a_cond3.sum())
print("Usuarios que dicen que NO tienen antispam y no lo tienen:", a_cond4.sum())
print("Usuarios que respondieron Ns/Nc:", a_cond5.sum())

# Total
a_total = a_cond1.sum() + a_cond2.sum() + a_cond3.sum() + a_cond4.sum() + a_cond5.sum()
print("Suma total de todos los usuarios en las combinaciones de antispam:", a_total)


# Asegurarnos de que los valores estén bien normalizados (sin espacios adicionales)
df_pc["b1_pc_4"] = df_pc["b1_pc_4"].str.strip()
df_pc["Antiespías_PC"] = df_pc["Antiespías_PC"].str.strip()
df_pc["Antifraude_PC"] = df_pc["Antifraude_PC"].str.strip()

# Crear una nueva columna que indique si tiene al menos uno de los dos
df_pc["Tiene_Antiespias_o_Antifraude"] = (
    (df_pc["Antiespías_PC"] == "Tiene") | (df_pc["Antifraude_PC"] == "Tiene")
)

# Combinaciones para ANTIESPÍAS o ANTIFRAUDE
e_cond1 = (df_pc["b1_pc_4"] == "Sí") & (df_pc["Tiene_Antiespias_o_Antifraude"])
e_cond2 = (df_pc["b1_pc_4"] == "Sí") & (~df_pc["Tiene_Antiespias_o_Antifraude"])
e_cond3 = (df_pc["b1_pc_4"] == "0.0") & (df_pc["Tiene_Antiespias_o_Antifraude"])
e_cond4 = (df_pc["b1_pc_4"] == "0.0") & (~df_pc["Tiene_Antiespias_o_Antifraude"])
e_cond5 = df_pc["b1_pc_4"].isin(["Ns/Nc"])

# Conteos
print("\n--- Análisis de ANTIESPÍAS o ANTIFRAUDE ---")
print("Usuarios que dicen que SÍ tienen protección y realmente tienen alguna:", e_cond1.sum())
print("Usuarios que dicen que SÍ tienen protección pero no tienen ninguna:", e_cond2.sum())
print("Usuarios que dicen que NO tienen protección pero sí tienen alguna:", e_cond3.sum())
print("Usuarios que dicen que NO tienen protección y no tienen ninguna:", e_cond4.sum())
print("Usuarios que respondieron Ns/Nc:", e_cond5.sum())

# Total
e_total = e_cond1.sum() + e_cond2.sum() + e_cond3.sum() + e_cond4.sum() + e_cond5.sum()
print("Suma total de todos los usuarios en las combinaciones de antiespías o antifraude:", e_total)
