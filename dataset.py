import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Define parameters
num_cameras = 5  # Number of cameras
num_motion_sensors = 10  # Number of motion sensors
num_door_window_sensors = 8  # Number of door/window sensors

# Generate timestamps for the dataset (100-150 rows)
start_date = datetime(2024, 1, 1)
timestamps = [start_date + timedelta(seconds=random.randint(0, 2592000)) for _ in range(0, 151)]

# Initialize an empty list to store all data
all_data = []

# Generate camera data
for ts in timestamps:
    for camera_id in range(1, num_cameras + 1):
        object_detected = random.choice(['Person', 'Vehicle', 'Animal', 'None'])
        all_data.append({'Timestamp': ts, 'SensorType': 'Camera', 'SensorID': camera_id, 'Event': object_detected})

# Generate motion sensor data
for ts in timestamps:
    for sensor_id in range(1, num_motion_sensors + 1):
        intensity = random.uniform(0, 1)
        all_data.append({'Timestamp': ts, 'SensorType': 'MotionSensor', 'SensorID': sensor_id, 'Event': intensity})

# Generate door/window sensor data
for ts in timestamps:
    for sensor_id in range(1, num_door_window_sensors + 1):
        event = random.choice(['Open', 'Close', 'None'])
        all_data.append({'Timestamp': ts, 'SensorType': 'DoorWindowSensor', 'SensorID': sensor_id, 'Event': event})

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(all_data)

# Save the DataFrame to a CSV file
df.to_csv('multi_sensor_data.csv', index=False)
