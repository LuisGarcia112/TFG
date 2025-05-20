import pandas as pd

# Rutas de los archivos CSV
ruta_jugadores = "juego_y_escaneo.csv"
ruta_totales = "Analisis.csv"

def analizar_archivo(ruta, nombre):
    # Leer los datos en pandas DataFrame
    df = pd.read_csv(ruta, encoding="utf-8")

    # Calcular la media de la edad, ignorando los valores NaN
    media_edad = df['c2_pcan'].mean()
    print(f"\nAnálisis para {nombre}:")
    print(f"La media de edad de los usuarios es: {media_edad:.2f}")

    # Filtrar las filas donde la columna 'a1_pcan_14' tenga el valor 'Sí'
    respuestas_si = df[df["a1_pcan_14"] == "Sí"]
    numero_respuestas_si = len(respuestas_si)
    print(f"El número de personas que afirman haber utilizado servicios de apuestas o casinos online en los últimos 6 meses es: {numero_respuestas_si} de {len(df)}")

    # Selección de preguntas relevantes
    preguntas = ['i6aan_1', 'i6aan_2', 'i6aan_5', 'i6aan_8', 'i6aan_9', 'i6ban_5', 'i6ban_6', 'i6ban_7']

    # Rellenar valores nulos con "NC"
    df[preguntas] = df[preguntas].fillna("NC")

    # Mapear respuestas de texto a números
    mapeo_respuestas = {
        "Nunca": 1, 
        "Rara vez": 2, 
        "Algunas veces": 3,
        "Bastantes veces": 4, 
        "La mayor parte del tiempo": 5, 
        "NC": 0
    }
    df[preguntas] = df[preguntas].applymap(lambda x: mapeo_respuestas.get(str(x).strip(), 0))

    # Clasificación basada en reglas
    df['adicto'] = df[preguntas].apply(
        lambda row: 2 if 0 in row.values else 1 if sum(row >= 4) >= 4 else 0,
        axis=1
    )

    clasificados = df['adicto'].value_counts()
    print("Resumen de clasificación de usuarios:")
    print(f"Usuarios clasificados como 'No Adicto' (0): {clasificados.get(0, 0)}")
    print(f"Usuarios clasificados como 'Adicto' (1): {clasificados.get(1, 0)}")
    print(f"Usuarios clasificados como 'No Contesta' (2): {clasificados.get(2, 0)}")

    # Pérdida económica promedio por usuario
    total_dinero = df['d2x_pcan_1'].sum() + df['d2x1_pcan_1'].sum()
    num_usuarios = len(df)
    perdida_media = total_dinero / num_usuarios
    print(f"La pérdida económica media por usuario es: {perdida_media:.2f} euros.")

# Ejecutar análisis para ambos archivos
analizar_archivo(ruta_jugadores, "jugadores")
analizar_archivo(ruta_totales, "totales")
