# from flask import Flask, Response
# from object_detection_model import ObjectDetection
# import cv2

# app = Flask(__name__)
# detector = ObjectDetection(capture_index=0)

# def generate_frames():
#     cap = cv2.VideoCapture(0)
#     assert cap.isOpened()
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
#         annotated_frame = detector.get_annotated_frame(frame)
#         _, buffer = cv2.imencode('.jpg', annotated_frame)
#         frame_encoded = buffer.tobytes()
#         yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame_encoded + b'\r\n')
#     cap.release()

# @app.route('/video_feed')
# def video_feed():
#     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5001, debug=True)

from flask import Flask,jsonify

import subprocess
import pymongo

from flask_cors import CORS

app = Flask(__name__)

CORS(app)

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

    # Convert retrieved incidents to a list of dictionaries
    incident_list = []
    for incident in incidents:
        # Convert ObjectId to string
        incident['_id'] = str(incident['_id'])
        incident_list.append(incident)

    return incident_list

@app.route('/incidents', methods=['GET'])
def get_incidents():
    # Retrieve all incidents
    incidents = retrieve_incidents()

    # Return incidents as JSON response
    return jsonify(incidents)

@app.route('/generate-csv', methods=['POST'])
def generate_csv():
    # Call your Python script to generate the CSV file here
    # Replace the following lines with your actual code
    # python_interpreter = '/usr/bin/python3'  # Example path to Python interpreter
    script_file = 'object_detection.py' 

    subprocess.run(['python3', script_file], stderr=subprocess.STDOUT)

@app.route('/',methods = ['GET'])
def alert_notifications():
    messsage = "Unknown user"
    return jsonify(messsage)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

