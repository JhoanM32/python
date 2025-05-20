import pandas as pd
import matplotlib.pyplot as plt

import requests



url = "https://jsonplaceholder.typicode.com/users"
  # Esta es una URL de ejemplo, tú debes poner la real


response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    print("Error al obtener los datos:", response.status_code)


data = pd.DataFrame({
    'Estudiantes': ['Ana','luis', 'Maria', 'Jorge', 'Sofia', 'Carlos'],
    'Matematicas':[3.5, 4.0, 3.8, 1.5, 2.3, 5.0],
    'Lenguaje':[5.0, 2.3, 1.5, 3.8, 4.0, 3.5],
    'Ciencias':[3.7, 4.0, 2.1, 1.5, 2.8, 3.1]
})

df= pd.DataFrame(data).set_index('Estudiantes')


df['Promedio_Materias']=df[['Matematicas','Lenguaje','Ciencias']].mean(axis=1)


Promedio_General = df['Promedio_Materias'].mean()
print(df)
print('Promedio_General = ', Promedio_General)

colores = ['red', 'orange', 'blue', 'green', 'purple', 'black']
#creando graficas
plt.bar(df.index, df['Promedio_Materias'], color=colores)
plt.xlabel('Estudiantes')#eje x del grafico
plt.ylabel('Promedio_Materias')#eje y del grafico
plt.title('PROMEDIO DE NOTAS POR ESTUDIANTES')#tituo de la grafico
plt.ylim(0,5)#Limite al eje y
plt.grid(axis='y')
plt.grid('x')

plt.show()  