from faker import Faker
import psycopg2
import os
import random
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

# Database connection setup
connection = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)
cursor = connection.cursor()

faker = Faker()

# Configuration options
vehicle_types = {
    "car": (40, 120),  # Speed range in km/h
    "truck": (30, 80),
    "motorcycle": (50, 140),
    "bus": (30, 90)
}

vehicle_sizes = ["light", "medium", "heavy"]

incident_types = ["accident", "construction", "event"]
severity_types = ["low", "medium", "high"]

weather_conditions = ["clear", "rain", "fog", "snow"]

area_types = ["urban", "rural", "highway"]

sensor_types = ["camera", "radar", "speed sensor"]
sensor_statuses = ["active", "inactive", "maintenance"]


# Functions for database interactions
def insert_sensors():
    for _ in range(10):
        lat = float(faker.latitude())  # Convert to float
        lon = float(faker.longitude())  # Convert to float
        sensor_type = random.choice(sensor_types)
        status = random.choice(sensor_statuses)
        installation_date = faker.date_between(start_date="-5y", end_date="today")
        update_frequency = random.choice([30, 60, 120])  # In seconds
        cursor.execute(
            """
            INSERT INTO sensors (location, type, status, installation_date, update_frequency)
            VALUES (ST_SetSRID(ST_Point(%s, %s), 4326), %s, %s, %s, %s)
            """,  # Correct ST_Point usage
            (lon, lat, sensor_type, status, installation_date, update_frequency)
        )
    connection.commit()
    print("Sensors inserted successfully.")



def insert_traffic_data():
    for _ in range(1000):
        sensor_id = random.randint(1, 10)
        vehicle_type = random.choice(list(vehicle_types.keys()))
        min_speed, max_speed = vehicle_types[vehicle_type]
        average_speed = round(random.uniform(min_speed, max_speed), 2)  # Limit to 2 decimals
        traffic_volume = random.randint(1, 100)
        visibility_km = round(random.uniform(0.5, 10.0), 2)  # Limit to 2 decimals
        area_type = random.choice(area_types)
        weather = random.choice(weather_conditions)
        vehicle_size = random.choice(vehicle_sizes)
        cursor.execute(
            """
            INSERT INTO traffic_data (sensor_id, timestamp, vehicle_type, duration_seconds, average_speed, 
                    traffic_volume, weather_conditions, visibility_km, vehicle_size, area_type)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                sensor_id,
                datetime.now() - timedelta(seconds=random.randint(0, 3600)),
                vehicle_type,
                random.randint(10, 600),
                average_speed,
                traffic_volume,
                weather,
                visibility_km,
                vehicle_size,
                area_type
            )
        )
    connection.commit()
    print("Traffic data inserted successfully.")


def insert_incidents():
    for _ in range(50):
        lat = float(faker.latitude())  # Aseguramos que sea float
        lon = float(faker.longitude())  # Aseguramos que sea float
        incident_type = random.choice(incident_types)
        severity = random.choice(severity_types)
        traffic_impact = round(random.uniform(10, 70), 2)  # % reducción del tráfico
        vehicles_affected = random.randint(1, 50)
        resolution_time = random.randint(10, 180)  # Tiempo de resolución en minutos
        duration_minutes = random.randint(10, 180)  # Duración del incidente en minutos

        # Consulta SQL corregida
        cursor.execute(
            """
            INSERT INTO incidents (location, type, timestamp, duration_minutes, severity, 
                                   traffic_impact_percentage, vehicles_affected, resolution_time_minutes)
            VALUES (ST_SetSRID(ST_Point(%s, %s), 4326), %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                lon, lat,  # Coordenadas
                incident_type,  # Tipo de incidente
                datetime.now(),  # Timestamp actual
                duration_minutes,  # Duración en minutos
                severity,  # Nivel de severidad
                traffic_impact,  # Impacto en porcentaje
                vehicles_affected,  # Vehículos afectados
                resolution_time  # Tiempo de resolución en minutos
            )
        )
    connection.commit()
    print("Incidents inserted successfully.")


def insert_areas():
    for _ in range(10):
        name = faker.city()
        population_density = random.randint(100, 10000)  # People per km²
        points_of_interest = faker.words(nb=random.randint(2, 5), unique=True)
        area_type = random.choice(area_types)
        cursor.execute(
            """
            INSERT INTO areas (name, population_density, points_of_interest, area_type)
            VALUES (%s, %s, %s, %s)
            """,
            (name, population_density, ', '.join(points_of_interest), area_type)
        )
    connection.commit()
    print("Areas inserted successfully.")


def insert_events():
    for _ in range(20):
        name = faker.catch_phrase()
        date = faker.date_time_between(start_date="now", end_date="+30d")
        lat = float(faker.latitude())  # Convert to float
        lon = float(faker.longitude())  # Convert to float
        expected_attendance = random.randint(50, 5000)
        cursor.execute(
            """
            INSERT INTO events (name, date, location, expected_attendance)
            VALUES (%s, %s, ST_SetSRID(ST_Point(%s, %s), 4326), %s)
            """,
            (name, date, lon, lat, expected_attendance)
        )
    connection.commit()
    print("Events inserted successfully.")



def insert_all():
    insert_sensors()
    insert_traffic_data()
    insert_incidents()
    insert_areas()
    insert_events()
    print("All data inserted successfully.")