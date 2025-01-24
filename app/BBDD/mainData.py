from tableCreator import create_tables
from dataInserts import insert_sensors, insert_traffic_data, insert_incidents, insert_areas, insert_events, insert_all
from dataDeletes import delete_data, delete_all
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

def show_menu():
    print("\n--- Menu ---")
    print("1. Create tables")
    print("2. Insert sensors")
    print("3. Insert traffic data")
    print("4. Insert incidents")
    print("5. Insert areas")
    print("6. Insert events")
    print("7. Insert all data")
    print("8. Delete data from a table")
    print("9. Delete all tables")
    print("10. Exit")

# Main loop
if __name__ == "__main__":
    while True:
        show_menu()
        option = input("Select an option: ")
        if option == "1":
            create_tables()
        elif option == "2":
            insert_sensors()
        elif option == "3":
            insert_traffic_data()
        elif option == "4":
            insert_incidents()
        elif option == "5":
            insert_areas()
        elif option == "6":
            insert_events()
        elif option == "7":
            insert_all()
        elif option == "8":
            table_name = input("Enter the table name to delete data from: ")
            delete_data(table_name)
        elif option == "9":
            delete_all()
        elif option == "10":
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please try again.")

    # Close connection and cursor
    cursor.close()
    connection.close()
