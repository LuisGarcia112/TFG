import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Datos de ejemplo: horas de estudio y si aprobaron el examen (0 = no aprobado, 1 = aprobado)
horas_estudio = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Horas de estudio
aprobado = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])  # 0 = no aprobado, 1 = aprobado

# Crear el modelo de regresión logística
modelo = LogisticRegression()

# Ajustar el modelo con los datos
modelo.fit(horas_estudio.reshape(-1, 1), aprobado)

# Generar un rango de horas de estudio (más detallado para la curva)
horas_rango = np.linspace(0, 11, 300).reshape(-1, 1)

# Probabilidad de aprobar calculada para los puntos originales (horas de estudio de los alumnos)
probabilidades_reales = modelo.predict_proba(horas_estudio.reshape(-1, 1))[:, 1]

# Predecir las probabilidades de aprobar el examen para cada hora de estudio (curva sigmoide)
probabilidades = modelo.predict_proba(horas_rango)[:, 1]  # Probabilidad de aprobar según el modelo

# Crear una lista de 15 alumnos con sus horas de estudio
alumnos_horas_estudio = np.array([2, 3, 4, 5, 6, 7, 8, 2, 9, 10, 1, 5, 6, 8, 3])  # Horas de estudio de 15 alumnos

# Calcular las probabilidades de aprobar para cada uno de los alumnos
probabilidades_alumnos = modelo.predict_proba(alumnos_horas_estudio.reshape(-1, 1))[:, 1]

# Clasificar a los alumnos según el umbral (0.5)
umbral = 0.5
aprobacion_alumnos = (probabilidades_alumnos >= umbral).astype(int)  # 1 = aprobado, 0 = no aprobado

# Mostrar los resultados
for i, horas in enumerate(alumnos_horas_estudio):
    estado = "Aprobado" if aprobacion_alumnos[i] == 1 else "No Aprobado"
    print(f"Alumno {i+1} - Horas de Estudio: {horas}, Predicción: {estado}")

# Crear el gráfico
plt.figure(figsize=(8, 6))

# Graficar la curva sigmoide (probabilidad de aprobar vs horas de estudio)
plt.plot(horas_rango, probabilidades, color='blue', label="Curva Sigmoide")

# Graficar los puntos de datos originales con sus probabilidades
plt.scatter(horas_estudio, probabilidades_reales, color='red', zorder=5, label="Probabilidad de Aprobar")

# Mostrar las probabilidades calculadas para los puntos originales
for i, txt in enumerate(probabilidades_reales):
    plt.annotate(f"{txt:.2f}", (horas_estudio[i], probabilidades_reales[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=9)

# Graficar el umbral (línea horizontal en 0.5)
plt.axhline(y=umbral, color='green', linestyle='--', label="Umbral (0.5)")

# Etiquetas y título
plt.title("Modelo de Regresión Logística: Probabilidad de Aprobar según Horas de Estudio")
plt.xlabel("Horas de Estudio")
plt.ylabel("Probabilidad de Aprobar")
plt.yticks(np.linspace(0, 1, 11))
plt.xticks(np.arange(0, 11, 1))

# Mostrar la leyenda
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()
