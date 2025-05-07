import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Cargar los datos desde el archivo CSV
file_path = "Datos_SMARTPHONE.csv"  
df = pd.read_csv(file_path, encoding="utf-8", sep=",")
df.columns = df.columns.str.strip()  # Limpiar nombres de columnas

# Selección de preguntas relevantes
preguntas = ['i6aan_1', 'i6aan_2', 'i6aan_5', 'i6aan_8', 'i6aan_9', 'i6ban_5', 'i6ban_6', 'i6ban_7']

# Mapear respuestas de texto a números
mapeo_respuestas = {
    "Nunca": 1, 
    "Rara vez": 2, 
    "Algunas veces": 3,
    "Bastantes veces": 4, 
    "La mayor parte del tiempo": 5
}

df[preguntas] = df[preguntas].applymap(lambda x: mapeo_respuestas.get(str(x).strip(), 0))

# Variable objetivo: clasificar usuarios en 0 (No Adicto) o 1 (Adicto)
df['adicto'] = df[preguntas].apply(
    lambda row: 1 if sum(row >= 4) >= 4 else 0,
    axis=1
)

# Preparar datos para el modelo
X = df[preguntas]  
y = df['adicto']  

# Dividir en entrenamiento y prueba (80% - 20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Verificar que hay al menos 2 clases en y_train
if len(set(y_train)) < 2:
    print("Error: y_train contiene solo una clase. No se puede entrenar el modelo.")
else:
    # Entrenar el modelo de regresión logística
    modelo = LogisticRegression()
    modelo.fit(X_train, y_train)

    # Hacer predicciones
    y_pred = modelo.predict(X_test)

    # Evaluar el modelo
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Precisión del modelo: {accuracy:.2f}")

    print("Matriz de confusión:")
    print(confusion_matrix(y_test, y_pred))

    print("Reporte de clasificación:")
    print(classification_report(y_test, y_pred))

    # Probar con un nuevo usuario (respuestas en texto)
    nuevo_usuario_texto = ["Bastantes veces", "La mayor parte del tiempo", "Algunas veces", "La mayor parte del tiempo", 
                           "Rara vez", "Bastantes veces", "Nunca", "La mayor parte del tiempo"]

    # Convertir texto a números
    nuevo_usuario_numerico = [mapeo_respuestas[resp] for resp in nuevo_usuario_texto]

    # Clasificar nuevo usuario
    clasificacion_nuevo_usuario = modelo.predict([nuevo_usuario_numerico])[0]

    # Mostrar resultado
    if clasificacion_nuevo_usuario == 1:
        print(f"Clasificación del nuevo usuario: Adicto")
    else:
        print(f"Clasificación del nuevo usuario: No Adicto")

    # Contar el número total de usuarios por categoría
    total_adictos = (df['adicto'] == 1).sum()
    total_no_adictos = (df['adicto'] == 0).sum()

    # Imprimir los resultados
    print(f"Total de usuarios clasificados como ADICTOS: {total_adictos}")
    print(f"Total de usuarios clasificados como NO ADICTOS: {total_no_adictos}")

    # Verificar si la suma coincide con el total de filas del dataset
    total_filas = len(df)
    total_clasificados = total_adictos + total_no_adictos
    print(f"Total de filas en el dataset: {total_filas}")
    print(f"Total de usuarios clasificados (sumados): {total_clasificados}")

    if total_filas == total_clasificados:
        print("El número de usuarios clasificados coincide con el total de filas.")
    else:
        print("Hay una discrepancia entre el número de usuarios clasificados y el total de filas.")

    # Obtener el directorio actual donde se ejecuta el script
    directorio_actual = os.path.dirname(os.path.abspath(__file__))

    # Filtrar usuarios adictos y no adictos
    usuarios_adictos = df[df['adicto'] == 1]
    usuarios_no_adictos = df[df['adicto'] == 0]

    # Exportar los CSV
    ruta_adictos = os.path.join(directorio_actual, "Usuarios_Adictos.csv")
    ruta_no_adictos = os.path.join(directorio_actual, "Usuarios_No_Adictos.csv")

    usuarios_adictos.to_csv(ruta_adictos, index=False)
    usuarios_no_adictos.to_csv(ruta_no_adictos, index=False)

    print(f"Datos exportados correctamente en:\n- {ruta_adictos}\n- {ruta_no_adictos}")

