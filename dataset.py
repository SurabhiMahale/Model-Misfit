import random
from datetime import datetime, timedelta

# Define sensor types and zones
sensor_types = ["Camera", "Motion Sensor", "Door Sensor", "Window Sensor"]
zones = ["Lobby", "Main Entrance", "Hallway", "Room 1", "Room 2"]

# Define possible object detections for cameras (optional)
objects = ["Person", "Vehicle", None]  # None for no object detected

def generate_event(base_time):
  """
  Generates a random sensor event with details.
  """
  # Randomly choose sensor type
  sensor_type = random.choice(sensor_types)

  # Randomly choose zone
  zone = random.choice(zones)

  # Generate random timestamp within a specific time range
  timestamp = base_time + timedelta(minutes=random.randint(0, 59))
  timestamp_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")

  # Additional details based on sensor type
  object_detected = None
  movement_detected = None
  open_closed = None

  if sensor_type == "Camera":
      object_detected = random.choice(objects)
  elif sensor_type == "Motion Sensor":
      movement_detected = "Yes" if random.random() < 0.7 else "No"
  elif sensor_type in ["Door Sensor", "Window Sensor"]:
      open_closed = "Open" if random.random() < 0.5 else "Closed"

  return {
      "Sensor Type": sensor_type,
      "Zone": zone,
      "Timestamp": timestamp_str,
      "Object Detected": object_detected,
      "Movement Detected": movement_detected,
      "Open/Closed": open_closed
  }


def generate_dataset(num_events, base_time=datetime(2024, 3, 18)):
  """
  Generates a list of sensor events for a specified number of events.
  """
  events = []
  for _ in range(num_events):
      event = generate_event(base_time)
      events.append(event)
  return events


# Generate a dataset with 50 events
dataset = generate_dataset(50)

# Print the dataset (optional)
# for event in dataset:
#   print(event)

# You can save the dataset to a CSV file using libraries like csv
import csv
with open('sensor_events.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=dataset[0].keys())
    writer.writeheader()
    writer.writerows(dataset)


