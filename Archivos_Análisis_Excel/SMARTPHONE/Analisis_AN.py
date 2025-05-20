import pandas as pd
import matplotlib.pyplot as plt
import mplcursors

# Cargar los archivos CSV de adictos, no adictos y usuarios totales
ruta_adictos = "Usuarios_Adictos.csv"
ruta_no_adictos = "Usuarios_No_Adictos.csv"
ruta_totales = "Datos_SMARTPHONE.csv"  

# Leer los datos en pandas DataFrames
df_adictos = pd.read_csv(ruta_adictos, encoding="utf-8")
df_no_adictos = pd.read_csv(ruta_no_adictos, encoding="utf-8")
df_totales = pd.read_csv(ruta_totales, encoding="utf-8")  

# --- Sección EDADES ---
# Calcular la edad media de los usuarios en cada archivo (usando la columna 'c2_pcan' para edad exacta)
edad_media_adictos = df_adictos['c2_pcan'].mean()
edad_media_no_adictos = df_no_adictos['c2_pcan'].mean()
edad_media_totales = df_totales['c2_pcan'].mean() 

# Mostrar la edad media
print(f"Edad media de los usuarios Adictos: {edad_media_adictos:.2f} años")
print(f"Edad media de los usuarios No Adictos: {edad_media_no_adictos:.2f} años")
print(f"Edad media de los usuarios Tercer Grupo: {edad_media_totales:.2f} años")  

# Limpiar los datos (eliminar espacios y convertir a minúsculas)
df_adictos['c2_pcan_edad_inter'] = df_adictos['c2_pcan_edad_inter'].str.strip().str.lower()
df_no_adictos['c2_pcan_edad_inter'] = df_no_adictos['c2_pcan_edad_inter'].str.strip().str.lower()
df_totales['c2_pcan_edad_inter'] = df_totales['c2_pcan_edad_inter'].str.strip().str.lower()  

# Definir los rangos de edad
rangos_edad = ['de 15 a 24 años', 'de 25 a 34 años', 'de 35 a 44 años', 'de 45 a 54 años', 'más de 55 años']

# Contar cuántas veces aparece cada valor en 'c2_pcan_edad_inter' para cada grupo
conteo_adictos = df_adictos['c2_pcan_edad_inter'].value_counts().reindex(rangos_edad, fill_value=0)
conteo_no_adictos = df_no_adictos['c2_pcan_edad_inter'].value_counts().reindex(rangos_edad, fill_value=0)
conteo_totales = df_totales['c2_pcan_edad_inter'].value_counts().reindex(rangos_edad, fill_value=0)  # Nuevo

# Crear los histogramas con 3 subplots
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

# Histograma del tercer grupo
plt.subplot(1, 3, 3)
plt.bar(conteo_totales.index, conteo_totales.values, color='orange')
plt.title("Distribución de edades (Total)")
plt.xlabel("Rango de edad")
plt.ylabel("Número de usuarios")
plt.xticks(rotation=45)

# Mostrar el gráfico
plt.tight_layout()

# Agregar interactividad
mplcursors.cursor(hover=True)

plt.show()

# Espera que el usuario presione una tecla para continuar
input("\nPresiona Enter para continuar a los datos de fraude económico")

# Cerrar los gráficos abiertos
plt.close('all')


# --- Sección fraude economico ---

# Calcular el valor medio de dinero perdido por usuario en los adictos
dinero_perdido_adictos = df_adictos[['d2x_pcan_1', 'd2x1_pcan_1']].sum().sum()
num_usuarios_adictos = len(df_adictos)
media_adictos = dinero_perdido_adictos / num_usuarios_adictos

# Calcular el valor medio de dinero perdido por usuario en los no adictos
dinero_perdido_no_adictos = df_no_adictos[['d2x_pcan_1', 'd2x1_pcan_1']].sum().sum()
num_usuarios_no_adictos = len(df_no_adictos)
media_no_adictos = dinero_perdido_no_adictos / num_usuarios_no_adictos

# Calcular el valor medio de dinero perdido por usuario del total
dinero_perdido_totales = df_totales[['d2x_pcan_1', 'd2x1_pcan_1']].sum().sum()
num_usuarios_totales = len(df_totales)
media_totales = dinero_perdido_totales / num_usuarios_totales

# Imprimir los resultados
print(f"Valor medio de dinero perdido por usuario (Adictos): {media_adictos:.2f} Euros por usuario")
print(f"Valor medio de dinero perdido por usuario (No Adictos): {media_no_adictos:.2f} Euros por usuario")
print(f"Valor medio de dinero perdido por usuario (Totales): {media_totales:.2f} Euros por usuario")

media_no_adictos_sin_100000_euros = (dinero_perdido_no_adictos - 100000) / (num_usuarios_no_adictos - 1)
print(f"Valor medio de dinero perdido por usuario (No Adictos) sin el outlier: {media_no_adictos_sin_100000_euros:.2f} Euros por usuario")

media_totales_sin_100000_euros = (dinero_perdido_totales - 100000) / (num_usuarios_totales - 1)
print(f"Valor medio de dinero perdido por usuario (Totales) sin el outlier: {media_totales_sin_100000_euros:.2f} Euros por usuario")

# Definir los rangos de edad en el orden correcto
rangos_edad = ["de 15 a 24 años", "de 25 a 34 años", "de 35 a 44 años", "de 45 a 54 años", "más de 55 años"]

# Función para calcular la pérdida media de dinero por rango de edad
def calcular_perdida_media(df):
    return df.groupby('c2_pcan_edad_inter')[['d2x_pcan_1', 'd2x1_pcan_1']].sum().sum(axis=1) / df['c2_pcan_edad_inter'].value_counts()

# Calcular la pérdida media por rango de edad para cada grupo
perdida_media_adictos = calcular_perdida_media(df_adictos).reindex(rangos_edad, fill_value=0)
perdida_media_no_adictos = calcular_perdida_media(df_no_adictos).reindex(rangos_edad, fill_value=0)
perdida_media_totales = calcular_perdida_media(df_totales).reindex(rangos_edad, fill_value=0)

# Crear los histogramas
plt.figure(figsize=(18, 6))

# Histograma de adictos
plt.subplot(1, 3, 1)
plt.bar(perdida_media_adictos.index, perdida_media_adictos.values, color='blue')
plt.title("Pérdida media de dinero por edad (Adictos)")
plt.xlabel("Rango de edad")
plt.ylabel("Pérdida media de dinero")
plt.xticks(rotation=45)

# Histograma de no adictos
plt.subplot(1, 3, 2)
plt.bar(perdida_media_no_adictos.index, perdida_media_no_adictos.values, color='green')
plt.title("Pérdida media de dinero por edad (No Adictos)")
plt.xlabel("Rango de edad")
plt.ylabel("Pérdida media de dinero")
plt.xticks(rotation=45)

# Histograma del tercer grupo
plt.subplot(1, 3, 3)
plt.bar(perdida_media_totales.index, perdida_media_totales.values, color='orange')
plt.title("Pérdida media de dinero por edad (Total)")
plt.xlabel("Rango de edad")
plt.ylabel("Pérdida media de dinero")
plt.xticks(rotation=45)

# Agregar interactividad
mplcursors.cursor(hover=True)

# Ajustar el diseño y mostrar el gráfico
plt.tight_layout()
plt.show()

# Espera que el usuario presione una tecla para continuar
input("\nPresiona Enter para continuar a los datos de infecciones del dispositivo")

# Cerrar los gráficos abiertos
plt.close('all')


# --- Sección infecciones del dispositvo ---

# Calcular la media de infecciones por dispositivo
media_infecciones_adictos = df_adictos["Totalinfecciones_AN"].mean()
media_infecciones_no_adictos = df_no_adictos["Totalinfecciones_AN"].mean()
media_infecciones_totales = df_totales["Totalinfecciones_AN"].mean()

# Imprimir los resultados
print(f"Media de infecciones por dispositivo en adictos: {media_infecciones_adictos:.2f}")
print(f"Media de infecciones por dispositivo en no adictos: {media_infecciones_no_adictos:.2f}")
print(f"Media de infecciones por dispositivo en usuarios totales: {media_infecciones_totales:.2f}")

# Contar infectados y no infectados en cada grupo
conteo_infectados_adictos = df_adictos["Infectado_AN"].value_counts()
conteo_infectados_no_adictos = df_no_adictos["Infectado_AN"].value_counts()
conteo_infectados_totales = df_totales["Infectado_AN"].value_counts()

# Crear la figura
plt.figure(figsize=(18, 6))

# Histograma de adictos
plt.subplot(1, 3, 1)
barras_adictos = plt.bar(conteo_infectados_adictos.index, conteo_infectados_adictos.values, color=['red', 'blue'])
plt.title("Dispositivos infectados (Adictos)")
plt.xlabel("Estado de infección")
plt.ylabel("Número de usuarios")

# Histograma de no adictos
plt.subplot(1, 3, 2)
barras_no_adictos = plt.bar(conteo_infectados_no_adictos.index, conteo_infectados_no_adictos.values, color=['red', 'blue'])
plt.title("Dispositivos infectados (No Adictos)")
plt.xlabel("Estado de infección")
plt.ylabel("Número de usuarios")

# Histograma de los usuarios totales
plt.subplot(1, 3, 3)
barras_tercer_grupo = plt.bar(conteo_infectados_totales.index, conteo_infectados_totales.values, color=['red', 'blue'])
plt.title("Dispositivos infectados (Totales)")
plt.xlabel("Estado de infección")
plt.ylabel("Número de usuarios")

# Agregar interactividad para mostrar valores
for barras in [barras_adictos, barras_no_adictos, barras_tercer_grupo]:
    cursor = mplcursors.cursor(barras, hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"{int(sel.target[1])}"))

plt.tight_layout()
plt.show()

# Definir las categorías de riesgo en orden
categorias_riesgo = ["No tiene Malware", "Riesgo Bajo", "Riesgo Medio", "Riesgo Alto"]

# Contar el número de usuarios en cada categoría de riesgo
conteo_riesgo_adictos = df_adictos["Riesgo_AN"].value_counts().reindex(categorias_riesgo, fill_value=0)
conteo_riesgo_no_adictos = df_no_adictos["Riesgo_AN"].value_counts().reindex(categorias_riesgo, fill_value=0)
conteo_riesgo_totales = df_totales["Riesgo_AN"].value_counts().reindex(categorias_riesgo, fill_value=0)

# Crear la figura para los histogramas
plt.figure(figsize=(18, 6))

# Histograma de adictos
plt.subplot(1, 3, 1)
barras_adictos = plt.bar(conteo_riesgo_adictos.index, conteo_riesgo_adictos.values, color=['green', 'yellow', 'orange', 'red'])
plt.title("Distribución de Riesgo (Adictos)")
plt.xlabel("Nivel de Riesgo")
plt.ylabel("Número de usuarios")
plt.xticks(rotation=45)

# Histograma de no adictos
plt.subplot(1, 3, 2)
barras_no_adictos = plt.bar(conteo_riesgo_no_adictos.index, conteo_riesgo_no_adictos.values, color=['green', 'yellow', 'orange', 'red'])
plt.title("Distribución de Riesgo (No Adictos)")
plt.xlabel("Nivel de Riesgo")
plt.ylabel("Número de usuarios")
plt.xticks(rotation=45)

# Histograma de los usuarios totales
plt.subplot(1, 3, 3)
barras_totales = plt.bar(conteo_riesgo_totales.index, conteo_riesgo_totales.values, color=['green', 'yellow', 'orange', 'red'])
plt.title("Distribución de Riesgo (Totales)")
plt.xlabel("Nivel de Riesgo")
plt.ylabel("Número de usuarios")
plt.xticks(rotation=45)

# Agregar interactividad
for barras in [barras_adictos, barras_no_adictos, barras_tercer_grupo]:
    cursor = mplcursors.cursor(barras, hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"{int(sel.target[1])}"))

# Ajustar diseño y mostrar el gráfico
plt.tight_layout()
plt.show()

# Espera que el usuario presione una tecla para continuar
input("\nPresiona Enter para continuar a los datos de la protección del dispositivo")

# Cerrar los gráficos abiertos

plt.close('all')

# --- Sección protección del dispositivo ---

# Asignar puntos por tener firewall, antivirus, antiespías, antispam, antifraude, h5d_pcan
def calcular_puntos_proteccion(df):
    df['puntos_firewall'] = df['Firewall_AN'].apply(lambda x: 2 if x == 'Tiene firewal activo' else 0)
    df['puntos_antivirus'] = df['Antivirus_AN'].apply(lambda x: 2 if (x != 'Ninguno' and pd.notna(x)) else 0)
    df['puntos_antiespias'] = df['Antiespia_AN'].apply(lambda x: 2 if x == 'Tiene' else 0)
    df['puntos_antispam'] = df['Antispam_AN'].apply(lambda x: 1 if x == 'Tiene' else 0)
    df['puntos_antifraude'] = df['Antifraude_AN'].apply(lambda x: 1 if x == 'Tiene' else 0)
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
        lambda x: 'Vulnerable' if x <= 3 else ('Protegido' if x <= 7 else 'Muy Protegido')
    )
    return df

# Aplicar a los tres grupos
df_adictos = calcular_puntos_proteccion(df_adictos)
df_no_adictos = calcular_puntos_proteccion(df_no_adictos)
df_totales = calcular_puntos_proteccion(df_totales)

# Calcular medias
media_adictos = df_adictos['puntos_proteccion'].mean()
media_no_adictos = df_no_adictos['puntos_proteccion'].mean()
media_totales = df_totales['puntos_proteccion'].mean()

# Imprimir medias
print(f"Puntuación media de protección para adictos: {media_adictos:.2f}")
print(f"Puntuación media de protección para no adictos: {media_no_adictos:.2f}")
print(f"Puntuación media de protección para tercer grupo: {media_totales:.2f}")

# Crear histogramas de clasificación
plt.figure(figsize=(18, 6))

# Adictos
plt.subplot(1, 3, 1)
conteo_adictos = df_adictos['clasificacion'].value_counts().reindex(['Vulnerable', 'Protegido', 'Muy Protegido'], fill_value=0)
barras_adictos = plt.bar(conteo_adictos.index, conteo_adictos.values, color=['red', 'yellow', 'green'])
plt.title("Clasificación de protección (Adictos)")
plt.xlabel("Clasificación")
plt.ylabel("Número de usuarios")
plt.xticks(rotation=45)

# No adictos
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
    cursor = mplcursors.cursor(barras, hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"{int(sel.target[1])}"))

plt.tight_layout()
plt.show()

# Crear histogramas de puntuaciones (0 a 9)
plt.figure(figsize=(18, 6))

# Adictos
plt.subplot(1, 3, 1)
conteo_puntos_adictos = df_adictos['puntos_proteccion'].value_counts().reindex(range(10), fill_value=0)
barras_adictos = plt.bar(conteo_puntos_adictos.index, conteo_puntos_adictos.values, color='blue')
plt.title("Distribución de puntuaciones de protección (Adictos)")
plt.xlabel("Puntuación")
plt.ylabel("Número de usuarios")

# No adictos
plt.subplot(1, 3, 2)
conteo_puntos_no_adictos = df_no_adictos['puntos_proteccion'].value_counts().reindex(range(10), fill_value=0)
barras_no_adictos = plt.bar(conteo_puntos_no_adictos.index, conteo_puntos_no_adictos.values, color='green')
plt.title("Distribución de puntuaciones de protección (No Adictos)")
plt.xlabel("Puntuación")
plt.ylabel("Número de usuarios")

# Tercer grupo
plt.subplot(1, 3, 3)
conteo_puntos_totales = df_totales['puntos_proteccion'].value_counts().reindex(range(10), fill_value=0)
barras_totales = plt.bar(conteo_puntos_totales.index, conteo_puntos_totales.values, color='purple')
plt.title("Distribución de puntuaciones de protección (Totales)")
plt.xlabel("Puntuación")
plt.ylabel("Número de usuarios")

# Interactividad
for barras in [barras_adictos, barras_no_adictos, barras_totales]:
    cursor = mplcursors.cursor(barras, hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"{int(sel.target[1])}"))

plt.tight_layout()
plt.show()
