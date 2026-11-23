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

print("---- grafica comida (X) Tiempo de copcinado (Y) 0099")
print("---- grafica comida (X) Texto a 30 grados 0099")
nombre_y_hora.plot.bar(x='name',y='cook_time', rot=30)
plt.title('COMIDA TIPICA DE INDIA ANAIS 0099 ')
plt.xlabel('NOMBRE PLATILLO')
plt.ylabel('TIEMPO DE COCINADFO')
plt.show()

nombre_y_hora_prep = df_food_india[['name', 'prep_time', 'cook_time']].head(10)
nombre_y_hora_prep.plot.bar(x='name', rot=30)
plt.title('Grafica der dos columnas  ANAIS 0099 ')
plt.xlabel('NOMBRE PLATILLO')
plt.ylabel('TIEMPO DE COCINADFO')
plt.show()

print("---- grafica apiladas una tras otra vereticalmente 0099")
nombre_y_hora_prep.plot.bar(x='name', stacked=True, rot=30)
plt.show()
