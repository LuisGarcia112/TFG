import pandas as pd
import matplotlib.pyplot as plt
import mplcursors

# Cargar los archivos CSV de adictos y no adictos
ruta_adictos = "Usuarios_Adictos.csv"
ruta_no_adictos = "Usuarios_No_Adictos.csv"

# Leer los datos en pandas DataFrames
df_adictos = pd.read_csv(ruta_adictos, encoding="utf-8")
df_no_adictos = pd.read_csv(ruta_no_adictos, encoding="utf-8")

# --- Sección EDADES ---
# Calcular la edad media de los usuarios en cada archivo (usando la columna 'c2_pcan' para edad exacta)
edad_media_adictos = df_adictos['c2_pcan'].mean()
edad_media_no_adictos = df_no_adictos['c2_pcan'].mean()

# Mostrar la edad media
print(f"Edad media de los usuarios Adictos: {edad_media_adictos:.2f} años")
print(f"Edad media de los usuarios No Adictos: {edad_media_no_adictos:.2f} años")

# Limpiar los datos (eliminar espacios y convertir a minúsculas)
df_adictos['c2_pcan_edad_inter'] = df_adictos['c2_pcan_edad_inter'].str.strip().str.lower()
df_no_adictos['c2_pcan_edad_inter'] = df_no_adictos['c2_pcan_edad_inter'].str.strip().str.lower()

# Definir los rangos de edad
rangos_edad = ['de 15 a 24 años', 'de 25 a 34 años', 'de 35 a 44 años', 'de 45 a 54 años', 'más de 55 años']

# Contar cuántas veces aparece cada valor en 'c2_pcan_edad_inter' para adictos
conteo_adictos = df_adictos['c2_pcan_edad_inter'].value_counts().reindex(rangos_edad, fill_value=0)

# Contar cuántas veces aparece cada valor en 'c2_pcan_edad_inter' para no adictos
conteo_no_adictos = df_no_adictos['c2_pcan_edad_inter'].value_counts().reindex(rangos_edad, fill_value=0)

# Crear los histogramas
plt.figure(figsize=(12, 6))

# Histograma de adictos
plt.subplot(1, 2, 1)
plt.bar(conteo_adictos.index, conteo_adictos.values, color='blue')
plt.title("Distribución de edades (Adictos)")
plt.xlabel("Rango de edad")
plt.ylabel("Número de usuarios")
plt.xticks(rotation=45)

# Histograma de no adictos
plt.subplot(1, 2, 2)
plt.bar(conteo_no_adictos.index, conteo_no_adictos.values, color='green')
plt.title("Distribución de edades (No Adictos)")
plt.xlabel("Rango de edad")
plt.ylabel("Número de usuarios")
plt.xticks(rotation=45)

# Mostrar el gráfico
plt.tight_layout()

# Agregar interactividad
import mplcursors
mplcursors.cursor(hover=True)

plt.show()

# Espera que el usuario presione una tecla para continuar
input("\nPresiona Enter para continuar a los datos de fraude económico")

# Cerrar los gráficos abiertos
plt.close('all')

# --- Sección fraude economico ---

# Calcular el valor medio de dinero perdido por usuario en los adictos
dinero_perdido_adictos = df_adictos[['d2x_pcan_1', 'd2x1_pcan_1']].sum().sum()  # Sumar todos los valores
num_usuarios_adictos = len(df_adictos)  # Número total de usuarios en adictos
media_adictos = dinero_perdido_adictos / num_usuarios_adictos  # Calcular el promedio

# Calcular el valor medio de dinero perdido por usuario en los no adictos
dinero_perdido_no_adictos = df_no_adictos[['d2x_pcan_1', 'd2x1_pcan_1']].sum().sum()  # Sumar todos los valores
num_usuarios_no_adictos = len(df_no_adictos)  # Número total de usuarios en no adictos
media_no_adictos = dinero_perdido_no_adictos / num_usuarios_no_adictos  # Calcular el promedio

# Imprimir los resultados
print(f"Valor medio de dinero perdido por usuario (Adictos): {media_adictos:.2f} Euros por usuario")
print(f"Valor medio de dinero perdido por usuario (No Adictos): {media_no_adictos:.2f} Euros por usuario")
print(f"Me parecia raro el resultado, hay un no adicto que ha perdido 100.000 euros")
media_no_adictos_sin_100000_euros = (dinero_perdido_no_adictos-100000) / (num_usuarios_no_adictos-1)  # Calcular el promedio
print(f"Valor medio de dinero perdido por usuario (No Adictos) quitando al de los 100000 euros: {media_no_adictos_sin_100000_euros:.2f} Euros por usuario")

# Definir los rangos de edad en el orden correcto
rangos_edad = ["de 15 a 24 años", "de 25 a 34 años", "de 35 a 44 años", "de 45 a 54 años", "más de 55 años"]

# Función para calcular la pérdida media de dinero por rango de edad
def calcular_perdida_media(df):
    return df.groupby('c2_pcan_edad_inter')[['d2x_pcan_1', 'd2x1_pcan_1']].sum().sum(axis=1) / df['c2_pcan_edad_inter'].value_counts()

# Calcular la pérdida media por rango de edad para adictos y no adictos
perdida_media_adictos = calcular_perdida_media(df_adictos).reindex(rangos_edad, fill_value=0)
perdida_media_no_adictos = calcular_perdida_media(df_no_adictos).reindex(rangos_edad, fill_value=0)

# Crear los histogramas
plt.figure(figsize=(12, 6))

# Histograma de adictos
plt.subplot(1, 2, 1)
bars_adictos = plt.bar(perdida_media_adictos.index, perdida_media_adictos.values, color='blue')
plt.title("Pérdida media de dinero por edad (Adictos)")
plt.xlabel("Rango de edad")
plt.ylabel("Pérdida media de dinero")
plt.xticks(rotation=45)

# Histograma de no adictos
plt.subplot(1, 2, 2)
bars_no_adictos = plt.bar(perdida_media_no_adictos.index, perdida_media_no_adictos.values, color='green')
plt.title("Pérdida media de dinero por edad (No Adictos)")
plt.xlabel("Rango de edad")
plt.ylabel("Pérdida media de dinero")
plt.xticks(rotation=45)

# Agregar interactividad para mostrar valores al pasar el ratón
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

# Imprimir los resultados
print(f"Media de infecciones por dispositivo en adictos: {media_infecciones_adictos:.2f}")
print(f"Media de infecciones por dispositivo en no adictos: {media_infecciones_no_adictos:.2f}")

# Contar infectados y no infectados en cada grupo
conteo_infectados_adictos = df_adictos["Infectado_AN"].value_counts()
conteo_infectados_no_adictos = df_no_adictos["Infectado_AN"].value_counts()

# Crear la figura
plt.figure(figsize=(12, 6))

# Histograma de adictos
plt.subplot(1, 2, 1)
barras_adictos = plt.bar(conteo_infectados_adictos.index, conteo_infectados_adictos.values, color=['red', 'blue'])
plt.title("Dispositivos infectados (Adictos)")
plt.xlabel("Estado de infección")
plt.ylabel("Número de usuarios")

# Histograma de no adictos
plt.subplot(1, 2, 2)
barras_no_adictos = plt.bar(conteo_infectados_no_adictos.index, conteo_infectados_no_adictos.values, color=['red', 'blue'])
plt.title("Dispositivos infectados (No Adictos)")
plt.xlabel("Estado de infección")
plt.ylabel("Número de usuarios")

# Agregar interactividad para mostrar valores
cursor_adictos = mplcursors.cursor(barras_adictos, hover=True)
cursor_no_adictos = mplcursors.cursor(barras_no_adictos, hover=True)

for cursor in [cursor_adictos, cursor_no_adictos]:
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"{int(sel.target[1])}"))

plt.tight_layout()
plt.show()


# Definir las categorías de riesgo en orden
categorias_riesgo = ["No tiene Malware", "Riesgo Bajo", "Riesgo Medio", "Riesgo Alto"]

# Contar el número de usuarios en cada categoría de riesgo
conteo_riesgo_adictos = df_adictos["Riesgo_AN"].value_counts().reindex(categorias_riesgo, fill_value=0)
conteo_riesgo_no_adictos = df_no_adictos["Riesgo_AN"].value_counts().reindex(categorias_riesgo, fill_value=0)

# Crear la figura para los histogramas
plt.figure(figsize=(12, 6))

# Histograma de adictos
plt.subplot(1, 2, 1)
barras_adictos = plt.bar(conteo_riesgo_adictos.index, conteo_riesgo_adictos.values, color=['green', 'yellow', 'orange', 'red'])
plt.title("Distribución de Riesgo (Adictos)")
plt.xlabel("Nivel de Riesgo")
plt.ylabel("Número de usuarios")
plt.xticks(rotation=45)

# Histograma de no adictos
plt.subplot(1, 2, 2)
barras_no_adictos = plt.bar(conteo_riesgo_no_adictos.index, conteo_riesgo_no_adictos.values, color=['green', 'yellow', 'orange', 'red'])
plt.title("Distribución de Riesgo (No Adictos)")
plt.xlabel("Nivel de Riesgo")
plt.ylabel("Número de usuarios")
plt.xticks(rotation=45)

# Agregar interactividad para mostrar valores al pasar el ratón
cursor_adictos = mplcursors.cursor(barras_adictos, hover=True)
cursor_no_adictos = mplcursors.cursor(barras_no_adictos, hover=True)

for cursor in [cursor_adictos, cursor_no_adictos]:
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"{int(sel.target[1])}"))

# Ajustar diseño y mostrar el gráfico
plt.tight_layout()
plt.show()


# Espera que el usuario presione una tecla para continuar
input("\nPresiona Enter para continuar a los datos de la protección del dispositivo")

# Cerrar los gráficos abiertos
plt.close('all')

# --- Sección protección del dipositivo---


# Asignar puntos por tener firewall, antivirus, antiespías, antispam, antifraude, h5d_pcan
def calcular_puntos_proteccion(df):
    # Puntos por firewall
    df['puntos_firewall'] = df['Firewall_AN'].apply(
        lambda x: 2 if x == 'Tiene firewal activo' else 0)
    
    # Puntos por antivirus
    df['puntos_antivirus'] = df['Antivirus_AN'].apply(
        lambda x: 2 if (x != 'Ninguno' and pd.notna(x)) else 0
    )
    
    # Puntos por antiespías
    df['puntos_antiespias'] = df['Antiespia_AN'].apply(
        lambda x: 2 if x == 'Tiene' else 0
    )
    
    # Puntos por antispam
    df['puntos_antispam'] = df['Antispam_AN'].apply(
        lambda x: 1 if x == 'Tiene' else 0
    )
    
    # Puntos por antifraude
    df['puntos_antifraude'] = df['Antifraude_AN'].apply(
        lambda x: 1 if x == 'Tiene' else 0
    )
    
    # Puntos por h5d_pcan
    df['puntos_h5d_pcan'] = df['h5d_pcan'].apply(
        lambda x: 1 if x == '2.0' else 0
    )
    
    # Calcular la puntuación total de protección
    df['puntos_proteccion'] = (
        df['puntos_firewall'] + 
        df['puntos_antivirus'] + 
        df['puntos_antiespias'] + 
        df['puntos_antispam'] + 
        df['puntos_antifraude'] + 
        df['puntos_h5d_pcan']
    )
    
    # Clasificación final basada en la puntuación total
    df['clasificacion'] = df['puntos_proteccion'].apply(
        lambda x: 'Vulnerable' if x <= 3 else ('Protegido' if x <= 7 else 'Muy Protegido')
    )
    
    return df

# Aplicar la función a los DataFrames de adictos y no adictos
df_adictos = calcular_puntos_proteccion(df_adictos)
df_no_adictos = calcular_puntos_proteccion(df_no_adictos)

# Calcular la puntuación media para adictos y no adictos
media_adictos = df_adictos['puntos_proteccion'].mean()
media_no_adictos = df_no_adictos['puntos_proteccion'].mean()

# Imprimir los resultados
print(f"Puntuación media de protección para adictos: {media_adictos:.2f}")
print(f"Puntuación media de protección para no adictos: {media_no_adictos:.2f}")


# Crear los histogramas para las clasificaciones de protección
plt.figure(figsize=(12, 6))

# Histograma de adictos
plt.subplot(1, 2, 1)
conteo_adictos = df_adictos['clasificacion'].value_counts().reindex(['Vulnerable', 'Protegido', 'Muy Protegido'], fill_value=0)
barras_adictos = plt.bar(conteo_adictos.index, conteo_adictos.values, color=['red', 'yellow', 'green'])
plt.title("Clasificación de protección (Adictos)")
plt.xlabel("Clasificación")
plt.ylabel("Número de usuarios")
plt.xticks(rotation=45)

# Histograma de no adictos
plt.subplot(1, 2, 2)
conteo_no_adictos = df_no_adictos['clasificacion'].value_counts().reindex(['Vulnerable', 'Protegido', 'Muy Protegido'], fill_value=0)
barras_no_adictos = plt.bar(conteo_no_adictos.index, conteo_no_adictos.values, color=['red', 'yellow', 'green'])
plt.title("Clasificación de protección (No Adictos)")
plt.xlabel("Clasificación")
plt.ylabel("Número de usuarios")
plt.xticks(rotation=45)

# Agregar interactividad para mostrar valores al pasar el ratón
cursor_adictos = mplcursors.cursor(barras_adictos, hover=True)
cursor_no_adictos = mplcursors.cursor(barras_no_adictos, hover=True)

# Definir lo que se debe mostrar cuando el ratón pasa por la barra
for cursor in [cursor_adictos, cursor_no_adictos]:
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"{int(sel.target[1])}"))

# Ajustar diseño y mostrar el gráfico
plt.tight_layout()
plt.show()

# Crear los histogramas para las puntuaciones (0 a 9) de protección
plt.figure(figsize=(12, 6))

# Histograma de adictos (puntuaciones de 0 a 9)
plt.subplot(1, 2, 1)
conteo_puntuaciones_adictos = df_adictos['puntos_proteccion'].value_counts().reindex(range(10), fill_value=0)
barras_adictos = plt.bar(conteo_puntuaciones_adictos.index, conteo_puntuaciones_adictos.values, color='blue')
plt.title("Distribución de puntuaciones de protección (Adictos)")
plt.xlabel("Puntuación")
plt.ylabel("Número de usuarios")

# Histograma de no adictos (puntuaciones de 0 a 9)
plt.subplot(1, 2, 2)
conteo_puntuaciones_no_adictos = df_no_adictos['puntos_proteccion'].value_counts().reindex(range(10), fill_value=0)
barras_no_adictos = plt.bar(conteo_puntuaciones_no_adictos.index, conteo_puntuaciones_no_adictos.values, color='green')
plt.title("Distribución de puntuaciones de protección (No Adictos)")
plt.xlabel("Puntuación")
plt.ylabel("Número de usuarios")

# Agregar interactividad para mostrar valores al pasar el ratón
cursor_adictos = mplcursors.cursor(barras_adictos, hover=True)
cursor_no_adictos = mplcursors.cursor(barras_no_adictos, hover=True)

# Definir lo que se debe mostrar cuando el ratón pasa por la barra
for cursor in [cursor_adictos, cursor_no_adictos]:
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"{int(sel.target[1])}"))

# Ajustar diseño y mostrar el gráfico
plt.tight_layout()
plt.show()