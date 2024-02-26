
from faker import Faker
import pandas as pd
import random

class Jugador:
    def __init__(self, nombre, numero_jugador, apellido, edad, provincia, categoria_jugador, porciento_ataque, porciento_defensa, porciento_saque, porciento_general):
        self.nombre = nombre
        self.numero_jugador = numero_jugador
        self.apellido = apellido
        self.edad = edad
        self.provincia = provincia
        self.categoria_jugador = categoria_jugador
        self.porciento_ataque = porciento_ataque
        self.porciento_defensa = porciento_defensa
        self.porciento_saque = porciento_saque
        self.porciento_general = porciento_general

    def to_dict(self):
        return {
            'Nombre': self.nombre,
            'Número de Jugador': self.numero_jugador,
            'Apellido': self.apellido,
            'Edad': self.edad,
            'Provincia': self.provincia,
            'Categoría de Jugador': self.categoria_jugador,
            'Porciento de Ataque': self.porciento_ataque,
            'Porciento de Defensa': self.porciento_defensa,
            'Porciento de Saque': self.porciento_saque,
            'Porciento General': self.porciento_general
        }

fake = Faker()

num_registros =  1000
datos_falsos = []

num_jugadores =  10
lista_jugadores = []

categorias_jugadores = ['Libero', 'Atacante', 'Sacador', 'Profesional']

for _ in range(num_jugadores):
    nombre = fake.name()
    numero_jugador = random.randint(1,  99)
    apellido = fake.last_name()
    edad = random.randint(18,  35)
    provincia = fake.state()
    categoria_jugador = random.choice(categorias_jugadores)
    porciento_ataque = random.randint(0,  100)
    porciento_defensa = random.randint(0,  100)
    porciento_saque = random.randint(0,  100)
    porciento_general = random.randint(0,  100)
    
    jugador = Jugador(nombre, numero_jugador, apellido, edad, provincia, categoria_jugador, porciento_ataque, porciento_defensa, porciento_saque, porciento_general)
    lista_jugadores.append(jugador)

tipos_entrenamiento = ['Peso', 'Aeróbico', 'Fuerza', 'Flexibilidad']
duraciones = ['30 minutos', '1 hora', '1 hora  30 minutos', '2 horas']
acciones = ['Correr', 'Saltar la cuerda', 'Hacer push-ups', 'Levantamiento de pesas']

for _ in range(num_registros):
    jugadores_dict = [jugador.to_dict() for jugador in lista_jugadores]  # Convertir cada Jugador en un diccionario
    id_entrenamiento = fake.random_int(min=1, max=1000, step=1)
    tipo_entrenamiento = random.choice(tipos_entrenamiento)
    duracion = random.choice(duraciones)
    acciones_entrenamiento = random.sample(acciones, random.randint(1, len(acciones)))
    propósito = fake.sentence()
    
    datos_falsos.append({
        'Lista de Jugadores': jugadores_dict,  # Almacenar la lista de diccionarios
        'id-entrenamiento': id_entrenamiento,
        'Tipo de entrenamiento': tipo_entrenamiento,
        'Duración': duracion,
        'Lista de Acciones': ', '.join(acciones_entrenamiento),
        'Propósito': propósito
    })

df = pd.DataFrame(datos_falsos)

# Exportar el DataFrame a un archivo CSV
df.to_csv('datos_entrenamientos.csv', index=False, encoding='utf-8')
