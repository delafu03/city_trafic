import psycopg2
from faker import Faker
import random
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

connection = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)
cursor = connection.cursor()

# Generar datos simulados
faker = Faker()
tipos_vehiculos = ["coche", "camión", "moto", "autobús"]
tipos_incidentes = ["accidente", "construcción", "evento"]

# Insertar sensores
for _ in range(10):
    lat, lon = faker.latitude(), faker.longitude()
    cursor.execute(
        "INSERT INTO sensores (ubicacion, tipo) VALUES (ST_Point(%s, %s), %s)",
        (lon, lat, random.choice(["cámara", "radar", "sensor de velocidad"]))
    )

# Insertar datos de tráfico
for _ in range(1000):
    cursor.execute(
        "INSERT INTO datos_trafico (sensor_id, hora, tipo_vehiculo, duracion_segundos, velocidad_promedio) "
        "VALUES (%s, %s, %s, %s, %s)",
        (
            random.randint(1, 10),  # sensor_id
            datetime.now() - timedelta(seconds=random.randint(0, 3600)),  # hora
            random.choice(tipos_vehiculos),
            random.randint(10, 600),  # duracion
            random.uniform(20, 120)  # velocidad promedio
        )
    )

# Insertar incidentes
for _ in range(50):
    lat, lon = faker.latitude(), faker.longitude()
    cursor.execute(
        "INSERT INTO incidentes (ubicacion, tipo, hora, duracion_minutos) "
        "VALUES (ST_Point(%s, %s), %s, %s, %s)",
        (lon, lat, random.choice(tipos_incidentes), datetime.now(), random.randint(10, 180))
    )

connection.commit()
cursor.close()
connection.close()
