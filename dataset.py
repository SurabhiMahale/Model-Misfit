import random
from datetime import datetime, timedelta
import csv


def generate_event(base_time):
    """
    Generates a random sensor event with details, ensuring no empty fields.
    """

    # Randomly choose sensor type
    sensor_type = random.choice(["Camera", "Motion Sensor", "Door Sensor", "Window Sensor"])

    # Randomly choose zone
    zone = random.choice(["Lobby", "Main Entrance", "Hallway", "Room 1", "Room 2"])

    # Generate random timestamp within a specific time range
    timestamp = base_time + timedelta(minutes=random.randint(0, 59))
    timestamp_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")

    # Ensure objects list for cameras is not empty
    objects = ["Person", "Vehicle", "door", "window", "bag"]  # Valid object detections

    # Additional details based on sensor type (no empty fields)
    event_data = {
        "Sensor Type": sensor_type,
        "Zone": zone,
        "Timestamp": timestamp_str,
    }

    if sensor_type == "Camera":
        event_data["Object Detected"] = random.choice(objects)  # Ensure object detection
    elif sensor_type == "Motion Sensor":
        event_data["Movement Detected"] = "Yes" if random.random() < 0.5 else "No"
    else:  # Door Sensor or Window Sensor
        event_data["Open/Closed"] = "Open" if random.random() < 0.5 else "Closed"

    return event_data  # All fields will have values


# ... rest of the code remains unchanged

def generate_event(base_time):
    """
    Generates a random sensor event with details, ensuring no empty fields.
    """

    # Randomly choose sensor type
    sensor_type = random.choice(["Camera", "Motion Sensor", "Door Sensor", "Window Sensor"])

    # Randomly choose zone
    zone = random.choice(["Lobby", "Main Entrance", "Hallway", "Room 1", "Room 2"])

    # Generate random timestamp within a specific time range
    timestamp = base_time + timedelta(minutes=random.randint(0, 59))
    timestamp_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")

    # Ensure objects list for cameras is not empty
    objects = ["Person", "Vehicle", "door", "window", "bag"]  # Valid object detections

    # Additional details based on sensor type (no empty fields)
    event_data = {
        "Sensor Type": sensor_type,
        "Zone": zone,
        "Timestamp": timestamp_str,
    }

    if sensor_type == "Camera":
        event_data["Object Detected"] = random.choice(objects)  # Ensure object detection
    elif sensor_type == "Motion Sensor":
        event_data["Movement Detected"] = "Yes" if random.random() < 0.7 else "No"
    else:  # Door Sensor or Window Sensor
        event_data["Open/Closed"] = "Open" if random.random() < 0.7 else "Closed"

    return event_data  # All fields will have values


# ... rest of the code remains unchanged


def generate_dataset(num_events, base_time=datetime(2024, 3, 18)):
    """
    Generates a list of sensor events for a specified number of events.
    """
    events = []
    for _ in range(num_events):
        event = generate_event(base_time)
        events.append(event)
    return events


# Generate a dataset with 100 events
dataset = generate_dataset(100)

# Get all unique field names from the dataset
fieldnames = set()
for event in dataset:
    fieldnames.update(event.keys())

# Write the dataset to a CSV file
with open("sensor_events.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=sorted(fieldnames))
    writer.writeheader()
    writer.writerows(dataset)

print("Sensor data generated and saved to sensor_events.csv")
