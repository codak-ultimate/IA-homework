from faker import Faker
import pandas as pd
import random

# Crear una instancia de Faker
fake = Faker()

# Número de registros falsos que deseas generar
num_registros =  1000

# Lista para almacenar los datos generados
datos_falsos = []

city=[]
city.append('Pinar del Rio')
city.append('Habana');
city.append('Villa Clara');
city.append('Camaguey');
city.append('Holguien');
city.append('Santiago de Cuba');
city.append('Granma');
city.append('Isla de la Juventud')
city.append('Guantanamo')
city.append('Matanzas');
city.append('Artemisa');
city.append('Mayabeque');
city.append('Cienfuegos')


for _ in range(num_registros):
    # Generar datos falsos para cada campo
    num_atleta = fake.random_int(min=1, max=700, step=1)  # Asumiendo que el número de atleta es un entero entre  1 y  100
    hora = fake.time()  # Genera una hora aleatoria
    fecha = fake.date()  # Genera una fecha aleatoria
    lugar = random.choice(city)  # Genera una ciudad aleatoria
    id_entrenamiento = fake.random_int(min=1, max=1000, step=1)  # Asumiendo que el ID de entrenamiento es un entero entre  1 y  1000
    
    # Agregar los datos generados a la lista
    datos_falsos.append({
        'num-atleta': num_atleta,
        'Hora': hora,
        'Fecha': fecha,
        'Lugar': lugar,
        'id-entrenamiento': id_entrenamiento,
    })

# Crear un DataFrame a partir de los datos generados
df = pd.DataFrame(datos_falsos)

# Exportar el DataFrame a un archivo CSV
df.to_csv('datos_entrenamientos.csv', index=False, encoding='utf-8')
