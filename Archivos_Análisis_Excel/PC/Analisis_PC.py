import pandas as pd
import matplotlib.pyplot as plt
import mplcursors

# Cargar los archivos CSV de adictos y no adictos
ruta_adictos = "Usuarios_Adictos.csv"
ruta_no_adictos = "Usuarios_No_Adictos.csv"
ruta_totales = "Datos_PC.csv"  # Archivo para los datos totales

# Leer los datos en pandas DataFrames
df_adictos = pd.read_csv(ruta_adictos, encoding="utf-8")
df_no_adictos = pd.read_csv(ruta_no_adictos, encoding="utf-8")
df_totales = pd.read_csv(ruta_totales)

# --- Sección EDADES ---
# Calcular la edad media de los usuarios en cada archivo
edad_media_adictos = df_adictos['c2_pcan'].mean()
edad_media_no_adictos = df_no_adictos['c2_pcan'].mean()
edad_media_totales = df_totales['c2_pcan'].mean()

# Mostrar la edad media
print(f"Edad media de los usuarios Adictos: {edad_media_adictos:.2f} años")
print(f"Edad media de los usuarios No Adictos: {edad_media_no_adictos:.2f} años")
print(f"Edad media de los usuarios Totales: {edad_media_totales:.2f} años")

# Limpiar los datos (eliminar espacios y convertir a minúsculas)
df_adictos['c2_pcan_edad_inter'] = df_adictos['c2_pcan_edad_inter'].str.strip().str.lower()
df_no_adictos['c2_pcan_edad_inter'] = df_no_adictos['c2_pcan_edad_inter'].str.strip().str.lower()
df_totales['c2_pcan_edad_inter'] = df_totales['c2_pcan_edad_inter'].str.strip().str.lower()

# Definir los rangos de edad
rangos_edad = ['de 15 a 24 años', 'de 25 a 34 años', 'de 35 a 44 años', 'de 45 a 54 años', 'más de 55 años']

# Contar cuántas veces aparece cada valor en 'c2_pcan_edad_inter'
conteo_adictos = df_adictos['c2_pcan_edad_inter'].value_counts().reindex(rangos_edad, fill_value=0)
conteo_no_adictos = df_no_adictos['c2_pcan_edad_inter'].value_counts().reindex(rangos_edad, fill_value=0)
conteo_totales = df_totales['c2_pcan_edad_inter'].value_counts().reindex(rangos_edad, fill_value=0)

# Crear los histogramas
plt.figure(figsize=(18, 6))

# Histograma de adictos
plt.subplot(1, 3, 1)
plt.bar(conteo_adictos.index, conteo_adictos.values, color='blue')
plt.title("Distribución de edades (Adictos)")
plt.xlabel("Rango de edad")
plt.ylabel("Número de usuarios")
plt.xticks(rotation=45)

# Histograma de no adictos
plt.subplot(1, 3, 2)
plt.bar(conteo_no_adictos.index, conteo_no_adictos.values, color='green')
plt.title("Distribución de edades (No Adictos)")
plt.xlabel("Rango de edad")
plt.ylabel("Número de usuarios")
plt.xticks(rotation=45)

# Histograma de totales
plt.subplot(1, 3, 3)
plt.bar(conteo_totales.index, conteo_totales.values, color='purple')
plt.title("Distribución de edades (Totales)")
plt.xlabel("Rango de edad")
plt.ylabel("Número de usuarios")
plt.xticks(rotation=45)

# Agregar interactividad
mplcursors.cursor(hover=True)

# Mostrar los gráficos
plt.tight_layout()
plt.show()

# Espera que el usuario presione una tecla para continuar
input("\nPresiona Enter para continuar a los datos de fraude económico")

# Cerrar los gráficos abiertos
plt.close('all')


# --- Sección fraude económico ---

# Calcular el valor medio de dinero perdido por usuario en los adictos
dinero_perdido_adictos = df_adictos[['d2x_pcan_1', 'd2x1_pcan_1']].sum().sum()
num_usuarios_adictos = len(df_adictos)
media_adictos = dinero_perdido_adictos / num_usuarios_adictos

# Calcular el valor medio de dinero perdido por usuario en los no adictos
dinero_perdido_no_adictos = df_no_adictos[['d2x_pcan_1', 'd2x1_pcan_1']].sum().sum()
num_usuarios_no_adictos = len(df_no_adictos)
media_no_adictos = dinero_perdido_no_adictos / num_usuarios_no_adictos

# Calcular el valor medio de dinero perdido por usuario en los totales
dinero_perdido_totales = df_totales[['d2x_pcan_1', 'd2x1_pcan_1']].sum().sum()
num_usuarios_totales = len(df_totales)
media_totales = dinero_perdido_totales / num_usuarios_totales

# Imprimir los resultados
print(f"Valor medio de dinero perdido por usuario (Adictos): {media_adictos:.2f} Euros por usuario")
print(f"Valor medio de dinero perdido por usuario (No Adictos): {media_no_adictos:.2f} Euros por usuario")
print(f"Valor medio de dinero perdido por usuario (Totales): {media_totales:.2f} Euros por usuario")


media_no_adictos_sin_10000_euros = (dinero_perdido_no_adictos - 10000) / (num_usuarios_no_adictos - 1)
print(f"Valor medio de dinero perdido por usuario (No Adictos) sin el outlier: {media_no_adictos_sin_10000_euros:.2f} Euros por usuario")

media_totales_sin_10000_euros = (dinero_perdido_totales - 10000) / (num_usuarios_totales - 1)
print(f"Valor medio de dinero perdido por usuario (Totales) sin el outlier: {media_totales_sin_10000_euros:.2f} Euros por usuario")

# Definir los rangos de edad
rangos_edad = ["de 15 a 24 años", "de 25 a 34 años", "de 35 a 44 años", "de 45 a 54 años", "más de 55 años"]

# Función para calcular la pérdida media de dinero por rango de edad
def calcular_perdida_media(df):
    total_perdido = df.groupby('c2_pcan_edad_inter')[['d2x_pcan_1', 'd2x1_pcan_1']].sum().sum(axis=1)
    cantidad_usuarios = df['c2_pcan_edad_inter'].value_counts()
    return (total_perdido / cantidad_usuarios).reindex(rangos_edad, fill_value=0)

# Calcular la pérdida media por edad
perdida_media_adictos = calcular_perdida_media(df_adictos)
perdida_media_no_adictos = calcular_perdida_media(df_no_adictos)
perdida_media_totales = calcular_perdida_media(df_totales)

# Crear los histogramas
plt.figure(figsize=(18, 6))

# Adictos
plt.subplot(1, 3, 1)
bars_adictos = plt.bar(perdida_media_adictos.index, perdida_media_adictos.values, color='blue')
plt.title("Pérdida media por edad (Adictos)")
plt.xlabel("Rango de edad")
plt.ylabel("Pérdida media (€)")
plt.xticks(rotation=45)

# No adictos
plt.subplot(1, 3, 2)
bars_no_adictos = plt.bar(perdida_media_no_adictos.index, perdida_media_no_adictos.values, color='green')
plt.title("Pérdida media por edad (No Adictos)")
plt.xlabel("Rango de edad")
plt.ylabel("Pérdida media (€)")
plt.xticks(rotation=45)

# Totales
plt.subplot(1, 3, 3)
bars_totales = plt.bar(perdida_media_totales.index, perdida_media_totales.values, color='purple')
plt.title("Pérdida media por edad (Totales)")
plt.xlabel("Rango de edad")
plt.ylabel("Pérdida media (€)")
plt.xticks(rotation=45)

# Agregar interactividad
mplcursors.cursor(hover=True)

# Mostrar el gráfico
plt.tight_layout()
plt.show()

# Espera para continuar
input("\nPresiona Enter para continuar a los datos de infecciones del dispositivo")
plt.close('all')

# --- Sección infecciones del dispositivo ---

# Calcular la media de infecciones por dispositivo
media_infecciones_adictos = df_adictos["Totalinfecciones_PC"].mean()
media_infecciones_no_adictos = df_no_adictos["Totalinfecciones_PC"].mean()
media_infecciones_totales = df_totales["Totalinfecciones_PC"].mean()

# Imprimir los resultados
print(f"Media de infecciones por dispositivo en Adictos: {media_infecciones_adictos:.2f}")
print(f"Media de infecciones por dispositivo en No Adictos: {media_infecciones_no_adictos:.2f}")
print(f"Media de infecciones por dispositivo en Totales: {media_infecciones_totales:.2f}")

# Contar infectados y no infectados
conteo_infectados_adictos = df_adictos["infectado_PC"].value_counts()
conteo_infectados_no_adictos = df_no_adictos["infectado_PC"].value_counts()
conteo_infectados_totales = df_totales["infectado_PC"].value_counts()

# Crear figura
plt.figure(figsize=(18, 6))

# Adictos
plt.subplot(1, 3, 1)
barras_adictos = plt.bar(conteo_infectados_adictos.index, conteo_infectados_adictos.values, color=['red', 'blue'])
plt.title("Dispositivos infectados (Adictos)")
plt.xlabel("Estado de infección")
plt.ylabel("Número de usuarios")

# No adictos
plt.subplot(1, 3, 2)
barras_no_adictos = plt.bar(conteo_infectados_no_adictos.index, conteo_infectados_no_adictos.values, color=['red', 'blue'])
plt.title("Dispositivos infectados (No Adictos)")
plt.xlabel("Estado de infección")
plt.ylabel("Número de usuarios")

# Totales
plt.subplot(1, 3, 3)
barras_totales = plt.bar(conteo_infectados_totales.index, conteo_infectados_totales.values, color=['red', 'blue'])
plt.title("Dispositivos infectados (Totales)")
plt.xlabel("Estado de infección")
plt.ylabel("Número de usuarios")

# Interactividad
for barras in [barras_adictos, barras_no_adictos, barras_totales]:
    mplcursors.cursor(barras, hover=True).connect("add", lambda sel: sel.annotation.set_text(f"{int(sel.target[1])}"))

plt.tight_layout()
plt.show()

# --- Sub-sección Riesgo del dispositivo ---

# Convertir Riesgo_PC a string por si hay valores numéricos
for df in [df_adictos, df_no_adictos, df_totales]:
    df["Riesgo_PC"] = df["Riesgo_PC"].astype(str)

# Categorías de riesgo y etiquetas
categorias_riesgo = ["0.0", "1.0", "2.0", "3.0"]
etiquetas_riesgo = ["Sin Riesgo", "Riesgo Bajo", "Riesgo Medio", "Riesgo Alto"]

# Contar usuarios por riesgo
conteo_riesgo_adictos = df_adictos["Riesgo_PC"].value_counts().reindex(categorias_riesgo, fill_value=0)
conteo_riesgo_no_adictos = df_no_adictos["Riesgo_PC"].value_counts().reindex(categorias_riesgo, fill_value=0)
conteo_riesgo_totales = df_totales["Riesgo_PC"].value_counts().reindex(categorias_riesgo, fill_value=0)

# Crear figura
plt.figure(figsize=(18, 6))

# Adictos
plt.subplot(1, 3, 1)
barras_adictos = plt.bar(etiquetas_riesgo, conteo_riesgo_adictos.values, color=['green', 'yellow', 'orange', 'red'])
plt.title("Distribución de Riesgo (Adictos)")
plt.xlabel("Nivel de Riesgo")
plt.ylabel("Número de usuarios")
plt.xticks(rotation=45)

# No adictos
plt.subplot(1, 3, 2)
barras_no_adictos = plt.bar(etiquetas_riesgo, conteo_riesgo_no_adictos.values, color=['green', 'yellow', 'orange', 'red'])
plt.title("Distribución de Riesgo (No Adictos)")
plt.xlabel("Nivel de Riesgo")
plt.ylabel("Número de usuarios")
plt.xticks(rotation=45)

# Totales
plt.subplot(1, 3, 3)
barras_totales = plt.bar(etiquetas_riesgo, conteo_riesgo_totales.values, color=['green', 'yellow', 'orange', 'red'])
plt.title("Distribución de Riesgo (Totales)")
plt.xlabel("Nivel de Riesgo")
plt.ylabel("Número de usuarios")
plt.xticks(rotation=45)

# Interactividad
for barras in [barras_adictos, barras_no_adictos, barras_totales]:
    mplcursors.cursor(barras, hover=True).connect("add", lambda sel: sel.annotation.set_text(f"{int(sel.target[1])}"))

plt.tight_layout()
plt.show()

# Continuar
input("\nPresiona Enter para continuar a los datos de la protección del dispositivo")
plt.close('all')


# --- Sección protección del dispositivo ---

# Función para calcular puntuación y clasificación
def calcular_puntos_proteccion(df):
    df['puntos_firewall'] = df['Firewal_PC'].apply(lambda x: 2 if x == 'Tiene firewal activo' else 0)
    df['puntos_antivirus'] = df['Antivirus_PC'].apply(lambda x: 2 if (x != 'Ninguno' and pd.notna(x)) else 0)
    df['puntos_antiespias'] = df['Antiespías_PC'].apply(lambda x: 1 if x == 'Tiene' else 0)
    df['puntos_antispam'] = df['Antispam_PC'].apply(lambda x: 1 if x == 'Tiene' else 0)
    df['puntos_antifraude'] = df['Antifraude_PC'].apply(lambda x: 1 if x == 'Tiene' else 0)
    df['puntos_h5d_pcan'] = df['h5d_pcan'].apply(lambda x: 1 if x == '2.0' else 0)
    
    df['puntos_proteccion'] = (
        df['puntos_firewall'] + 
        df['puntos_antivirus'] + 
        df['puntos_antiespias'] + 
        df['puntos_antispam'] + 
        df['puntos_antifraude'] + 
        df['puntos_h5d_pcan']
    )
    
    df['clasificacion'] = df['puntos_proteccion'].apply(
        lambda x: 'Vulnerable' if x <= 4 else ('Protegido' if x <= 6 else 'Muy Protegido')
    )
    
    return df

# Aplicar a los tres grupos
df_adictos = calcular_puntos_proteccion(df_adictos)
df_no_adictos = calcular_puntos_proteccion(df_no_adictos)
df_totales = calcular_puntos_proteccion(df_totales)

# Medias
media_adictos = df_adictos['puntos_proteccion'].mean()
media_no_adictos = df_no_adictos['puntos_proteccion'].mean()
media_totales = df_totales['puntos_proteccion'].mean()

# Mostrar resultados
print(f"Puntuación media de protección para Adictos: {media_adictos:.2f}")
print(f"Puntuación media de protección para No Adictos: {media_no_adictos:.2f}")
print(f"Puntuación media de protección para Totales: {media_totales:.2f}")

# --- Gráfico de clasificación (Vulnerable / Protegido / Muy Protegido) ---

plt.figure(figsize=(18, 6))

# Adictos
plt.subplot(1, 3, 1)
conteo_adictos = df_adictos['clasificacion'].value_counts().reindex(['Vulnerable', 'Protegido', 'Muy Protegido'], fill_value=0)
barras_adictos = plt.bar(conteo_adictos.index, conteo_adictos.values, color=['red', 'yellow', 'green'])
plt.title("Clasificación de protección (Adictos)")
plt.xlabel("Clasificación")
plt.ylabel("Número de usuarios")
plt.xticks(rotation=45)

# No Adictos
plt.subplot(1, 3, 2)
conteo_no_adictos = df_no_adictos['clasificacion'].value_counts().reindex(['Vulnerable', 'Protegido', 'Muy Protegido'], fill_value=0)
barras_no_adictos = plt.bar(conteo_no_adictos.index, conteo_no_adictos.values, color=['red', 'yellow', 'green'])
plt.title("Clasificación de protección (No Adictos)")
plt.xlabel("Clasificación")
plt.ylabel("Número de usuarios")
plt.xticks(rotation=45)

# Totales
plt.subplot(1, 3, 3)
conteo_totales = df_totales['clasificacion'].value_counts().reindex(['Vulnerable', 'Protegido', 'Muy Protegido'], fill_value=0)
barras_totales = plt.bar(conteo_totales.index, conteo_totales.values, color=['red', 'yellow', 'green'])
plt.title("Clasificación de protección (Totales)")
plt.xlabel("Clasificación")
plt.ylabel("Número de usuarios")
plt.xticks(rotation=45)

# Interactividad
for barras in [barras_adictos, barras_no_adictos, barras_totales]:
    mplcursors.cursor(barras, hover=True).connect("add", lambda sel: sel.annotation.set_text(f"{int(sel.target[1])}"))

plt.tight_layout()
plt.show()

# --- Gráfico de puntuación (0 a 9) ---

plt.figure(figsize=(18, 6))

# Adictos
plt.subplot(1, 3, 1)
conteo_puntos_adictos = df_adictos['puntos_proteccion'].value_counts().reindex(range(10), fill_value=0)
barras_adictos = plt.bar(conteo_puntos_adictos.index, conteo_puntos_adictos.values, color='blue')
plt.title("Distribución de puntuaciones de protección (Adictos)")
plt.xlabel("Puntuación")
plt.ylabel("Número de usuarios")

# No Adictos
plt.subplot(1, 3, 2)
conteo_puntos_no_adictos = df_no_adictos['puntos_proteccion'].value_counts().reindex(range(10), fill_value=0)
barras_no_adictos = plt.bar(conteo_puntos_no_adictos.index, conteo_puntos_no_adictos.values, color='green')
plt.title("Distribución de puntuaciones de protección (No Adictos)")
plt.xlabel("Puntuación")
plt.ylabel("Número de usuarios")

# Totales
plt.subplot(1, 3, 3)
conteo_puntos_totales = df_totales['puntos_proteccion'].value_counts().reindex(range(10), fill_value=0)
barras_totales = plt.bar(conteo_puntos_totales.index, conteo_puntos_totales.values, color='orange')
plt.title("Distribución de puntuaciones de protección (Totales)")
plt.xlabel("Puntuación")
plt.ylabel("Número de usuarios")

# Interactividad
for barras in [barras_adictos, barras_no_adictos, barras_totales]:
    mplcursors.cursor(barras, hover=True).connect("add", lambda sel: sel.annotation.set_text(f"{int(sel.target[1])}"))

plt.tight_layout()
plt.show()
