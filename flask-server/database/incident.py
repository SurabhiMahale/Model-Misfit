import pymongo
from datetime import datetime

# Assuming MongoDB is running on localhost on default port 27017
# client = pymongo.MongoClient("mongodb+srv://nishant123:nishant123@firstproject.wami2av.mongodb.net/?retryWrites=true&w=majority&appName=firstproject")
# db = client["incidentDB"]

# incidents_collection = db["incidents"]

# Example of incident data
incidents = [
    {"incidentName": "Fire detected", "timestamp": "2024-03-17T09:45:00Z"},
    {"incidentName": "Mob detected", "timestamp": "2024-03-16T16:30:00Z"},
    {"incidentName": "Unknown access", "timestamp": "2024-03-16T13:05:00Z"},
    {"incidentName": "Fire detected", "timestamp": "2024-03-17T10:00:00Z"},
    {"incidentName": "Mob detected", "timestamp": "2024-03-16T16:45:00Z"},
    {"incidentName": "Unknown access", "timestamp": "2024-03-16T13:20:00Z"},
    {"incidentName": "Fire detected", "timestamp": "2024-03-17T10:15:00Z"},
    {"incidentName": "Mob detected", "timestamp": "2024-03-16T17:00:00Z"},
    {"incidentName": "Unknown access", "timestamp": "2024-03-16T13:35:00Z"},
    {"incidentName": "Fire detected", "timestamp": "2024-03-17T10:30:00Z"}
]


def insert_incident(incident_name, db_url="mongodb+srv://nishant123:nishant123@firstproject.wami2av.mongodb.net/?retryWrites=true&w=majority&appName=firstproject", db_name="incidentDB", collection_name="incidents"):
    # Connect to MongoDB
    client = pymongo.MongoClient(db_url)
    db = client[db_name]
    incidents_collection = db[collection_name]

    # Create incident document
    incident = {
        "incidentName": incident_name,
        "timestamp": datetime.now()
    }

    # Insert the incident document into the collection
    result = incidents_collection.insert_one(incident)
    print("Inserted document ID:", result.inserted_id)

def retrieve_incidents(incident_name=None, db_url="mongodb+srv://nishant123:nishant123@firstproject.wami2av.mongodb.net/?retryWrites=true&w=majority&appName=firstproject", db_name="incidentDB", collection_name="incidents"):
    # Connect to MongoDB
    client = pymongo.MongoClient(db_url)
    db = client[db_name]
    incidents_collection = db[collection_name]

    # Query to retrieve incidents
    query = {}
    if incident_name:
        query["incidentName"] = incident_name

    # Retrieve incidents based on the query
    incidents = incidents_collection.find(query)

    # Display retrieved incidents
    for incident in incidents:
        print(incident)


incidents_to_insert = [
    "Fire detected",
    "Mob detected",
    "Unknown access",
    "Fire detected",
    "Mob detected",
    "Unknown access",
    "Fire detected",
    "Mob detected",
    "Unknown access",
    "Fire detected",
    "Mob detected",
    "Unknown access"
]

# Insert each incident
# for incident in incidents_to_insert:
#     insert_incident(incident)

# print(retrieve_incidents())