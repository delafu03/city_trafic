import psycopg2
import os
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

def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sensors (
        id SERIAL PRIMARY KEY,
        location GEOMETRY(Point, 4326),
        type VARCHAR(50),
        status VARCHAR(20),
        installation_date DATE,
        update_frequency INT
    );
    
    CREATE TABLE IF NOT EXISTS traffic_data (
        id SERIAL PRIMARY KEY,
        sensor_id INT REFERENCES sensors(id),
        timestamp TIMESTAMP,
        vehicle_type VARCHAR(50),
        duration_seconds INT,
        average_speed NUMERIC(5, 2),
        traffic_volume INT,
        weather_conditions VARCHAR(50),
        visibility_km NUMERIC(5, 2),
        vehicle_size VARCHAR(50),
        area_type VARCHAR(20)
    );
    
    CREATE TABLE IF NOT EXISTS incidents (
        id SERIAL PRIMARY KEY,
        location GEOMETRY(Point, 4326),
        type VARCHAR(50),
        timestamp TIMESTAMP,
        duration_minutes INT,
        severity VARCHAR(20),
        traffic_impact_percentage NUMERIC(5, 2),
        vehicles_affected INT,
        resolution_time_minutes INT
    );

    CREATE TABLE IF NOT EXISTS areas (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        population_density INT,
        points_of_interest TEXT,
        area_type VARCHAR(20)
    );

    CREATE TABLE IF NOT EXISTS events (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        date TIMESTAMP,
        location GEOMETRY(Point, 4326),
        expected_attendance INT
    );
    """)
    connection.commit()
    print("Tables created successfully.")