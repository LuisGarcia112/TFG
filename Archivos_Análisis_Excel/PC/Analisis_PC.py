import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Cargar los datos desde el archivo CSV
file_path = "Datos_PC.csv"
df = pd.read_csv(file_path, encoding="utf-8", sep=",")
df.columns = df.columns.str.strip()

# Definir la variable relevante
variable_uso = "uso5_pcan"

# Mapear las respuestas a valores binarios (1 = Adicto, 0 = No Adicto)
mapeo_uso = {
    "Menos de 1 hora": 0,
    "Entre 1 y 5 horas": 0,
    "Entre 5 y 20 horas": 0,
    "Entre 20 y 40 horas": 1,
    "Más de 40 horas": 1
}

df["adicto"] = df[variable_uso].map(mapeo_uso)

# Preparar datos para el modelo
X = df[[variable_uso]].apply(lambda x: x.map(mapeo_uso))  # Convertir respuestas a numéricas
y = df["adicto"]

# Dividir en entrenamiento y prueba (80% - 20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

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

# Contar el número total de usuarios por categoría
total_adictos = (df['adicto'] == 1).sum()
total_no_adictos = (df['adicto'] == 0).sum()

# Imprimir los resultados
print(f"Total de usuarios clasificados como ADICTOS: {total_adictos}")
print(f"Total de usuarios clasificados como NO ADICTOS: {total_no_adictos}")

# Verificar que el número de clasificados coincida con el total de filas
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

# Exportar los CSV en la misma carpeta del script
ruta_adictos = os.path.join(directorio_actual, "Usuarios_Adictos.csv")
ruta_no_adictos = os.path.join(directorio_actual, "Usuarios_No_Adictos.csv")

usuarios_adictos.to_csv(ruta_adictos, index=False)
usuarios_no_adictos.to_csv(ruta_no_adictos, index=False)

print(f"Datos exportados correctamente en:\n- {ruta_adictos}\n- {ruta_no_adictos}")