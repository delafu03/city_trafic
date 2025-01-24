# Prerequisites

- Python 3.8 or higher
- PostgreSQL database with `postgis` extension enabled
- Required Python packages: `requirements.txt`

---

# Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

# 1. Create a virtual environment

To create a virtual environment in Python, follow these steps:

1. Open a terminal and navigate to your project directory.
2. (A) Run the following command to create a virtual environment named `.venv`:

   ```bash
   python -m venv .venv
   ```

3. (B) Open the VS Code command palette with `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (macOS) and type `Python: Create Environment`: select the `Python: Create Environment` option and choose the `./.venv` option to create a virtual environment in the `.venv` folder.

4. Activate the virtual environment:

   - On Windows:

     ```bash
     .\.venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source .venv/bin/activate
     ```

5. Once activated, you will see the name of the virtual environment in the command line.

6. Navigate to the folder containing the `requirements.txt` file:

   ```bash
   cd path/to/requirements.txt
   ```

7. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

To deactivate the virtual environment, simply run:

```bash
deactivate
```

# 2. Traffic Data Management System

## Overview

This project provides a Python-based system to manage traffic-related data, including sensors, traffic data, incidents, areas, and events. It includes utilities for creating database tables, inserting realistic data, and clearing tables when needed.

The project is divided into several Python scripts:

- `tableCreator.py`: Handles database table creation.
- `dataInserts.py`: Handles insertion of data into various tables.
- `dataDeletes.py`: Provides utilities for deleting data from tables.
- `mainData.py`: Main script for interacting with the system via a command-line menu.

---

## File Structure

### `tableCreator.py`

- **Purpose**: Defines the database schema and creates necessary tables.
- **Key Function**:
  - `create_tables`: Creates the following tables if they do not already exist:
    - `sensors`: Contains sensor details (e.g., type, status, location).
    - `traffic_data`: Records traffic-related metrics (e.g., speed, volume, visibility).
    - `incidents`: Logs incidents affecting traffic (e.g., accidents, construction).
    - `areas`: Stores information about different zones (e.g., population density).
    - `events`: Tracks events that may influence traffic (e.g., concerts, sports).

---

### `dataInserts.py`

- **Purpose**: Simulates and inserts realistic data into the tables.
- **Key Functions**:
  - `insert_sensors`: Inserts data about traffic sensors, including type, status, and location.
  - `insert_traffic_data`: Adds traffic data (e.g., speed, volume) and conditions (e.g., weather, area type).
  - `insert_incidents`: Logs incidents with details like severity, traffic impact, and vehicles affected.
  - `insert_areas`: Adds area information, including population density and points of interest.
  - `insert_events`: Records events with details like location, expected attendance, and time.
  - `insert_all`: Calls all insertion functions to populate every table.

---

### `dataDeletes.py`

- **Purpose**: Provides functionality to delete data from tables.
- **Key Functions**:
  - `delete_data(table_name)`: Deletes all data from the specified table.
  - `delete_all`: Clears all data from all tables (`traffic_data`, `incidents`, `sensors`, `areas`, and `events`).

---

### `mainData.py`

- **Purpose**: Provides a menu-driven interface for interacting with the system.
- **Menu Options**:
  1. **Create Tables**: Calls `create_tables` to ensure all tables exist.
  2. **Insert Sensors**: Calls `insert_sensors` to populate the `sensors` table.
  3. **Insert Traffic Data**: Calls `insert_traffic_data` to populate `traffic_data`.
  4. **Insert Incidents**: Calls `insert_incidents` to populate `incidents`.
  5. **Insert Areas**: Calls `insert_areas` to populate `areas`.
  6. **Insert Events**: Calls `insert_events` to populate `events`.
  7. **Insert All Data**: Calls `insert_all` to populate all tables.
  8. **Delete Data From Table**: Prompts the user for a table name and deletes its data.
  9. **Delete All Tables**: Calls `delete_all` to clear all tables.
  10. **Exit**: Ends the program.

---

# 3. Database Tables Information

## **Database Tables**

The system uses a PostgreSQL database with the following tables. Each table serves a specific purpose related to traffic data management. Below is an explanation of each table and its columns.

---

### **1. `sensors`**

This table stores information about traffic sensors deployed in different locations.

| Column              | Type              | Description                                                       |
| ------------------- | ----------------- | ----------------------------------------------------------------- |
| `id`                | `SERIAL`          | Unique identifier for the sensor.                                 |
| `location`          | `GEOMETRY(Point)` | Geographic location of the sensor (latitude and longitude).       |
| `type`              | `VARCHAR(50)`     | Type of the sensor (e.g., camera, radar, speed sensor).           |
| `status`            | `VARCHAR(20)`     | Operational status of the sensor (active, inactive, maintenance). |
| `installation_date` | `DATE`            | Date when the sensor was installed.                               |
| `update_frequency`  | `INT`             | Frequency of updates from the sensor (in seconds).                |

---

### **2. `traffic_data`**

This table stores real-time traffic data collected by sensors.

| Column               | Type            | Description                                                             |
| -------------------- | --------------- | ----------------------------------------------------------------------- |
| `id`                 | `SERIAL`        | Unique identifier for the traffic data entry.                           |
| `sensor_id`          | `INT`           | Reference to the `id` column in the `sensors` table.                    |
| `timestamp`          | `TIMESTAMP`     | Time when the data was recorded.                                        |
| `vehicle_type`       | `VARCHAR(50)`   | Type of vehicle detected (e.g., car, truck, motorcycle, bus).           |
| `duration_seconds`   | `INT`           | Time duration the data covers (in seconds).                             |
| `average_speed`      | `NUMERIC(5, 2)` | Average speed of vehicles (in km/h).                                    |
| `traffic_volume`     | `INT`           | Total number of vehicles detected during the duration.                  |
| `weather_conditions` | `VARCHAR(50)`   | Weather conditions during data collection (e.g., clear, rain, fog).     |
| `visibility_km`      | `NUMERIC(5, 2)` | Visibility in kilometers during data collection.                        |
| `vehicle_size`       | `VARCHAR(50)`   | Size of the vehicles (e.g., light, medium, heavy).                      |
| `area_type`          | `VARCHAR(20)`   | Type of area where the sensor is located (e.g., urban, rural, highway). |

---

### **3. `incidents`**

This table logs information about traffic incidents.

| Column                      | Type              | Description                                                   |
| --------------------------- | ----------------- | ------------------------------------------------------------- |
| `id`                        | `SERIAL`          | Unique identifier for the incident.                           |
| `location`                  | `GEOMETRY(Point)` | Geographic location of the incident (latitude and longitude). |
| `type`                      | `VARCHAR(50)`     | Type of incident (e.g., accident, construction, event).       |
| `timestamp`                 | `TIMESTAMP`       | Time when the incident was reported.                          |
| `duration_minutes`          | `INT`             | Duration of the incident (in minutes).                        |
| `severity`                  | `VARCHAR(20)`     | Severity level of the incident (low, medium, high).           |
| `traffic_impact_percentage` | `NUMERIC(5, 2)`   | Percentage reduction in traffic flow due to the incident.     |
| `vehicles_affected`         | `INT`             | Number of vehicles affected by the incident.                  |
| `resolution_time_minutes`   | `INT`             | Time it took to resolve the incident (in minutes).            |

---

### **4. `areas`**

This table stores information about geographic areas.

| Column               | Type           | Description                                                   |
| -------------------- | -------------- | ------------------------------------------------------------- |
| `id`                 | `SERIAL`       | Unique identifier for the area.                               |
| `name`               | `VARCHAR(100)` | Name of the area (e.g., city, district).                      |
| `population_density` | `INT`          | Population density of the area (people per km²).              |
| `points_of_interest` | `TEXT`         | Points of interest in the area (e.g., landmarks, facilities). |
| `area_type`          | `VARCHAR(20)`  | Type of area (e.g., urban, rural, highway).                   |

---

### **5. `events`**

This table logs information about events that may impact traffic.

| Column                | Type              | Description                                                |
| --------------------- | ----------------- | ---------------------------------------------------------- |
| `id`                  | `SERIAL`          | Unique identifier for the event.                           |
| `name`                | `VARCHAR(100)`    | Name of the event (e.g., concert, sports game).            |
| `date`                | `TIMESTAMP`       | Date and time of the event.                                |
| `location`            | `GEOMETRY(Point)` | Geographic location of the event (latitude and longitude). |
| `expected_attendance` | `INT`             | Number of attendees expected at the event.                 |

---

### **How to Use the Tables**

1. **Sensors and Data Collection**:
   - Sensors (`sensors`) collect traffic data (`traffic_data`) at specific locations.
2. **Incidents and Events**:
   - Incidents (`incidents`) and events (`events`) provide context for anomalies in traffic patterns.
3. **Geographic Areas**:
   - Areas (`areas`) provide regional context for traffic data, such as population density and landmarks.
