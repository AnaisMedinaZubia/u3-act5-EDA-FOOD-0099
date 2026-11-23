import pandas as pd
import matplotlib.pyplot as plt
# Anais Medina NC 0099
# 1. Leer el archivo CSV comida pais india
df_food_india = pd.read_csv('indian_food.csv')
print("\n--- DATOS LEÍDOS DESDE CSV, comida de india 0099 ---")
print(df_food_india)
print("\n--- Mostrar nombre, comida + ingredientes  0099 ---")
recetas = df_food_india[['name', 'ingredients']]
print(recetas)
print("---- Tienpo de coccion mostrar  10 registros con head 0099")
nombre_y_hora = df_food_india [['name', 'cook_time']].head(10)
print(nombre_y_hora)