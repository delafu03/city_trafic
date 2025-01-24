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

def delete_data(table_name):
    cursor.execute(f"DELETE FROM {table_name}")
    connection.commit()
    print(f"Data from table '{table_name}' deleted successfully.")


def delete_all():
    tables = ["traffic_data", "incidents", "sensors", "areas", "events"]  # List all table names
    for table in tables:
        cursor.execute(f"DELETE FROM {table}")
    connection.commit()
    print("All tables cleared successfully.")